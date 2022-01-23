from bubble_sort import Solution

example = Solution()

def test_single_sort_c1():
    assert example.single_sort([4, 3, 2, 1], 4) == [3, 2, 1, 4]

def test_single_sort_c2():
    assert example.single_sort([2, 4, 3, 1], 4) == [2, 3, 1, 4]

def test_single_sort_c3():
    assert example.single_sort([3, 1, 2, 4], 4) == [1, 2, 3, 4]

def test_single_sort_c4():
    assert example.single_sort([3, 2, 1, 4], 4) == [2, 1, 3, 4]




def test_complete_sort_c1():
    assert example.complete_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_complete_sort_c2():
    assert example.complete_sort([2, 4, 3, 1]) == [1, 2, 3, 4]

def test_complete_sort_c3():
    assert example.complete_sort([3, 1, 2, 4]) == [1, 2, 3, 4]

def test_complete_sort_c4():
    assert example.complete_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
