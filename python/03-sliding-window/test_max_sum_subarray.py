from max_sum_subarray import max_sum_subarray, max_sum_subarray_brute_force

def test_max_sum_subarray():
    assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9

def test_max_sum_subarray_k_equals_length():
    assert max_sum_subarray([1, 2, 3], 3) == 6

def test_brute_force_matches():
    assert max_sum_subarray_brute_force([2, 1, 5, 1, 3, 2], 3) == 9
