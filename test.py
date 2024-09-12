import pytest
from hw2.hw2_debugging import merge_sort

def test_merge_sort():
    assert merge_sort([5, 3, 2, 1, 8]) == [1, 2, 3, 5, 8]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 1, 1, 1, 2, 3, 4]) == [1, 1, 1, 2, 3, 4, 5]
