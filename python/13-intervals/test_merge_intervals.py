from merge_intervals import merge_intervals, merge_intervals_recursive

def test_merges_overlapping_intervals():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_merges_touching_boundary():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]

def test_leaves_non_overlapping_unchanged():
    assert merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def test_empty_input():
    assert merge_intervals([]) == []

def test_recursive_matches():
    assert merge_intervals_recursive([[1, 3], [2, 6], [8, 10], [15, 18]]) == \
        [[1, 6], [8, 10], [15, 18]]
