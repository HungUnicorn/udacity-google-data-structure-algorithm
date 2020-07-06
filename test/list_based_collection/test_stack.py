from src.list_based_collection.linked_list import Element
import pytest

from src.list_based_collection.stack import Stack


@pytest.fixture
def stack():
    e1 = Element(1)

    stack = Stack(e1)
    return stack


def test_stack_op(stack):
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    stack.push(e2)
    stack.push(e3)

    assert 3 == stack.pop().value
    assert 2 == stack.pop().value
    assert 1 == stack.pop().value

    stack.pop()
    stack.push(e4)
    assert 4 == stack.pop().value
