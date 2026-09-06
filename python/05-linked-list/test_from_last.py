from linked_list import LinkedList
from from_last import from_last, from_last_two_pass

def build_list():
    l = LinkedList()
    for x in ['a', 'b', 'c', 'd']:
        l.insert_last(x)
    return l

def test_from_last():
    l = build_list()
    assert from_last(l, 2).data == 'b'

def test_from_last_zero():
    l = build_list()
    assert from_last(l, 0).data == 'd'

def test_from_last_two_pass_matches():
    l = build_list()
    assert from_last_two_pass(l, 2).data == 'b'
