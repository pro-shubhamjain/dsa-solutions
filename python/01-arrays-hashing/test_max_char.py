from max_char import max_char, max_char_sorted

def test_max_char():
    assert max_char('abcccccccd') == 'c'

def test_max_char_sorted_matches():
    assert max_char_sorted('abcccccccd') == 'c'
