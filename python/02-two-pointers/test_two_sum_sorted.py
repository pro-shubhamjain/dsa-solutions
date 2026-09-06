from two_sum_sorted import two_sum, two_sum_hash_map

def test_two_sum():
    assert two_sum([1, 2, 4, 6, 8, 9], 11) == [1, 5]

def test_two_sum_no_match():
    assert two_sum([1, 2, 3], 100) == []

def test_two_sum_hash_map_matches_on_unsorted():
    assert two_sum_hash_map([4, 1, 9, 6, 2, 8], 11) == [2, 4]
