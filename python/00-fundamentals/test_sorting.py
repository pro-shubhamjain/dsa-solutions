from sorting import bubble_sort, selection_sort, merge_sort

INPUT = [100, -40, 500, -124, 0, 21, 7]
EXPECTED = [-124, -40, 0, 7, 21, 100, 500]

def test_bubble_sort():
    assert bubble_sort(INPUT.copy()) == EXPECTED

def test_selection_sort():
    assert selection_sort(INPUT.copy()) == EXPECTED

def test_merge_sort():
    assert merge_sort(INPUT.copy()) == EXPECTED
