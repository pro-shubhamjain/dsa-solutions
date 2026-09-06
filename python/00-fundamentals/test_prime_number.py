from prime_number import is_prime, is_prime_optimized

def test_is_prime_true_cases():
    assert is_prime(2) is True
    assert is_prime(17) is True

def test_is_prime_false_cases():
    assert is_prime(1) is False
    assert is_prime(15) is False

def test_is_prime_optimized_matches():
    for n in range(-2, 30):
        assert is_prime(n) == is_prime_optimized(n)
