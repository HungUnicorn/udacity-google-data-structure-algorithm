import pytest

from src.search_sort.binary_search import binary_search


@pytest.fixture
def input_list():
    test_list = [1, 3, 9, 11, 15, 19, 29]
    return test_list


def test_binary_search(input_list):
    test_val1 = 25
    test_val2 = 15
    assert -1 == binary_search(input_list, test_val1)
    assert 4 == binary_search(input_list, test_val2)
