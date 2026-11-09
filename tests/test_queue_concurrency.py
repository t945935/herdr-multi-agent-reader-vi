from concurrent.futures import ThreadPoolExecutor

from examples.queue import Queue


def test_concurrent_conflicting_enqueue_rejects_second_payload(tmp_path):
    queue = Queue(tmp_path / "jobs.db")

    def enqueue(number):
        try:
            queue.enqueue("same-key", {"numbers": [number]})
            return "accepted"
        except ValueError:
            return "conflict"

    with ThreadPoolExecutor(max_workers=2) as executor:
        states = sorted(executor.map(enqueue, [1, 2]))
    assert states == ["accepted", "conflict"]
    assert len(queue.jobs()) == 1
