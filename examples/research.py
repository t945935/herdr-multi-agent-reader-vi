"""Chương 8: xác thực bằng chứng gắn luận điểm với nguồn và tạo báo cáo có thể kiểm tra."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("Cần có câu hỏi nghiên cứu")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("Cần có nguồn")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("Thông tin nguồn chưa đầy đủ")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("URL nguồn phải dùng HTTP hoặc HTTPS")
        if source["id"] in by_id:
            raise ValueError("ID nguồn bị trùng")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("Cần có luận điểm")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("Luận điểm không hợp lệ")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Luận điểm được hỗ trợ phải có bằng chứng")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("Bằng chứng cần nguồn đã biết và trích dẫn")
    return by_id


def render(data):
    sources = validate(data)
    lines = ["# " + data["question"], "", "## Findings and Evidence", ""]
    for claim in data["claims"]:
        lines.extend([f"### {claim['text']}", "", "Status: " + claim["status"], ""])
        for evidence in claim.get("evidence", []):
            source = sources[evidence["source"]]
            lines.extend([f"> {evidence['quote']}", "", f"Source: [{source['title']}]({source['url']})", ""])
    lines.extend(["## Sources", ""])
    for source in sources.values():
        lines.append(f"- {source['id']}：[{source['title']}]({source['url']})；{source['kind']}；accessed {source['accessed']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = render(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(args.output)
