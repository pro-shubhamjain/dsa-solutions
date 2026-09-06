from even_odd import check_even_odd, print_even_odd

def test_check_even_odd_even():
    assert check_even_odd(4) == 'Even number'

def test_check_even_odd_odd():
    assert check_even_odd(7) == 'Odd number'

def test_check_even_odd_invalid():
    assert check_even_odd(0) == 'Not valid number'
    assert check_even_odd(-2) == 'Not valid number'

def test_print_even_odd():
    assert print_even_odd(2) == ['1: Odd Number', '2: Even Number']
