import pytest

from src.list_based_collection.queue import Queue


@pytest.fixture
def q():
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q


def test_peek(q):
    assert 1 == q.peek()


def test_deque(q):
    assert 1 == q.dequeue()


def test_enqueue(q):
    q.enqueue(4)
    assert 1 == q.dequeue()
    assert 2 == q.dequeue()
    assert 3 == q.dequeue()
    assert 4 == q.dequeue()

    q.enqueue(5)
    assert 5 == q.peek()
