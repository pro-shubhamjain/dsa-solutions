from anagrams import anagrams, anagrams_frequency_map

def test_anagrams_true():
    assert anagrams('hello', 'llohe') is True

def test_anagrams_false():
    assert anagrams('hello', 'world') is False

def test_anagrams_frequency_map_matches():
    assert anagrams_frequency_map('hello', 'llohe') is True
    assert anagrams_frequency_map('hello', 'world') is False
