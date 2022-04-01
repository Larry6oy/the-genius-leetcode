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

def test_mergeSort_c1():
    assert example.mergeSort([]) == []

def test_mergeSort_c2():
    assert example.mergeSort([1]) == [1]

def test_mergeSort_c3():
    assert example.mergeSort([2, 1]) == [1, 2]

def test_mergeSort_c4():
    assert example.mergeSort([3, 1, 2]) == [1, 2, 3]

def test_mergeSort_c5():
    assert example.mergeSort([4, 3, 1, 2]) == [1, 2, 3, 4]

def test_mergeSort_c6():
    assert example.mergeSort([1, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergeSort_c7():
    assert example.mergeSort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergeSort_c8():
    assert example.mergeSort([3, 1, 5, 2, 6]) == [1, 2, 3, 5, 6]

def test_mergeSort_c9():
    assert example.mergeSort([1, 3, 2, 5]) == [1, 2, 3, 5]

def test_mergeSort_c10():
    assert example.mergeSort([1, 5, 3]) == [1, 3, 5]

def test_mergeSort_c11():
    assert example.mergeSort([1, 3, 4, 3]) == [1, 3, 3, 4]
