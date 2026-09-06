from fizzbuzz import fizz_buzz_list

def test_fizzbuzz_basic():
    assert fizz_buzz_list(5) == [1, 2, 'fizz', 4, 'buzz']

def test_fizzbuzz_fizzbuzz_case():
    assert fizz_buzz_list(15)[14] == 'fizzbuzz'
