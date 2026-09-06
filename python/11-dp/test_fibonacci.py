from fibonacci import fibonacci, fibonacci_cache

def test_fibonacci_naive():
    assert fibonacci(4) == 3
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_cache():
    assert fibonacci_cache(10) == 55

def test_both_match():
    for i in range(10):
        assert fibonacci(i) == fibonacci_cache(i)
