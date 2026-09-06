from palindrome import palindrome, palindrome_two_pointer

def test_palindrome_true():
    assert palindrome('aba') is True

def test_palindrome_false():
    assert palindrome('abc') is False

def test_palindrome_two_pointer_matches():
    assert palindrome_two_pointer('aba') is True
    assert palindrome_two_pointer('abc') is False
