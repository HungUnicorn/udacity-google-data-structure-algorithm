from src.list.linked_list import Element, LinkedList
import pytest


@pytest.fixture
def ll():
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    return ll


def test_get_position(ll):
    assert ll.head.next.next.value == ll.get_position(3).value


def test_insert(ll):
    e4 = Element(4)
    ll.insert(e4, 3)

    assert 4 == ll.get_position(3).value


def test_delete(ll):
    ll.delete(1)

    assert 2 == ll.get_position(1).value
    assert 3 == ll.get_position(2).value
