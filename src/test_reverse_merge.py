from doctest import Example
from reverse_merge import Solution

example = Solution()

def test_reverseMerge_c1():
    assert example.reverseMerge([]) == []

def test_reverseMerge_c2():
    assert example.reverseMerge([1]) == [1]

def test_reverseMerge_c3():
    assert example.reverseMerge([2, 1]) == [2, 1]

def test_reverseMerge_c4():
    assert example.reverseMerge([3, 1, 2]) == [3, 2, 1]

def test_reverseMerge_c5():
    assert example.reverseMerge([4, 3, 1, 2]) == [4, 3, 2, 1]

def test_reverseMerge_c6():
    assert example.reverseMerge([1, 3, 2, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverseMerge_c7():
    assert example.reverseMerge([4, 5, 3, 2, 1]) == [5, 4, 3, 2 ,1]

def test_reverseMerge_c8():
    assert example.reverseMerge([3, 1, 5, 2, 6]) == [6, 5, 3, 2, 1]

def test_reverseMerge_c9():
    assert example.reverseMerge([1, 3, 2, 5]) == [5, 3, 2, 1]

def test_reverseMerge_c10():
    assert example.reverseMerge([1, 5, 3]) == [5, 3, 1]

def test_reverseMerge_c11():
    assert example.reverseMerge([1, 3, 4, 3]) == [4, 3, 3, 1]