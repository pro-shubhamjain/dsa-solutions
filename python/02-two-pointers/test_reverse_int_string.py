from reverse_int_string import reverse_string, reverse_integer

def test_reverse_string():
    assert reverse_string('abcd') == 'dcba'

def test_reverse_integer_positive():
    assert reverse_integer(90) == 9

def test_reverse_integer_negative():
    assert reverse_integer(-2359) == -9532

def test_reverse_integer_zero():
    assert reverse_integer(0) == 0
