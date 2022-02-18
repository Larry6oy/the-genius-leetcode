from merge_sort import Solution

example = Solution()

def test_sortTwoArray_t1():
    assert example.mergeTwoArray([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

def test_sortTwoArray_t2():
    assert example.mergeTwoArray([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

def test_sortTwoArray_t3():
    assert example.mergeTwoArray([1, 3, 5], [2, 6]) == [1, 2, 3, 5, 6]

def test_sortTwoArray_t4():
    assert example.mergeTwoArray([1, 3, 5], [2]) == [1, 2, 3, 5]

def test_sortTwoArray_t5():
    assert example.mergeTwoArray([1, 3, 5], []) == [1, 3, 5]