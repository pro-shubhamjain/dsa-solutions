from find_vowels import count_vowels

def test_count_vowels():
    assert count_vowels('aeiou') == 5

def test_count_vowels_none():
    assert count_vowels('xyz') == 0
