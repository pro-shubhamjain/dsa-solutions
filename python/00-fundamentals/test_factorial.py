from factorial import factorial, factorial_recur

def test_factorial_base_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_of_5():
    assert factorial(5) == 120

def test_factorial_negative():
    assert factorial(-3) == "Factorial is not defined for negative numbers"

def test_factorial_recur_matches():
    assert factorial_recur(5) == 120
    assert factorial_recur(0) == 1
