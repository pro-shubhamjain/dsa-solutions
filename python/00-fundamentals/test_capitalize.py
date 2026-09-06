from capitalize import capitalize, capitalize_loop

def test_capitalize():
    assert capitalize("hi there, how is it going?") == "Hi There, How Is It Going?"

def test_capitalize_loop_matches():
    assert capitalize_loop("hi there, how is it going?") == "Hi There, How Is It Going?"

def test_capitalize_empty_string():
    assert capitalize_loop("") == ""
