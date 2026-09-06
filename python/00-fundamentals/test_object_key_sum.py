from object_key_sum import obj_key_sum, obj_key_sum_defaultdict

def test_obj_key_sum():
    assert obj_key_sum([{'a': 2}, {'a': 2}, {'b': 1}, {'b': 9}]) == {'a': 4, 'b': 10}

def test_obj_key_sum_defaultdict_matches():
    assert obj_key_sum_defaultdict([{'a': 2}, {'a': 2}, {'b': 1}, {'b': 9}]) == {'a': 4, 'b': 10}
