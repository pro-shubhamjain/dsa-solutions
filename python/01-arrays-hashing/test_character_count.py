from character_count import count_char_serialize, count_all_char

def test_count_char_serialize():
    assert count_char_serialize('abbbccddddaab') == 'a1b3c2d4a2b1'

def test_count_all_char():
    result = count_all_char('aabbbc')
    assert result == {'a': 2, 'b': 3, 'c': 1}
