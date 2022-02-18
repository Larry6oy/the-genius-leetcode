
from binary_sort import Solution

example = Solution()


def test_sortArray_c1():
    assert example.sortArray([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_sortArray_c2():
    assert example.sortArray([2, 4, 3, 1]) == [1, 2, 3, 4]

def test_sortArray_c3():
    assert example.sortArray([3, 1, 2, 4]) == [1, 2, 3, 4]

def test_sortArray_c4():
    assert example.sortArray([3, 2, 1, 4]) == [1, 2, 3, 4]