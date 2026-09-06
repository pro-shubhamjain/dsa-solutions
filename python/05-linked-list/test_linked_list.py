from linked_list import LinkedList

def test_insert_first():
    l = LinkedList()
    l.insert_first('a')
    l.insert_first('b')
    assert l.get_first().data == 'b'
    assert l.size() == 2

def test_insert_last_and_get_last():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    assert l.get_last().data == 'b'

def test_remove_first():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    l.remove_first()
    assert l.get_first().data == 'b'

def test_remove_last():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    l.remove_last()
    assert l.get_last().data == 'a'
    assert l.size() == 1

def test_get_at_and_remove_at():
    l = LinkedList()
    for x in ['a', 'b', 'c']:
        l.insert_last(x)
    assert l.get_at(1).data == 'b'
    l.remove_at(1)
    assert l.get_at(1).data == 'c'
    assert l.size() == 2

def test_insert_at():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('c')
    l.insert_at('b', 1)
    assert l.get_at(1).data == 'b'
    assert l.size() == 3

def test_clear():
    l = LinkedList()
    l.insert_last('a')
    l.clear()
    assert l.size() == 0
    assert l.get_first() is None

def test_for_each():
    l = LinkedList()
    for x in [1, 2, 3]:
        l.insert_last(x)
    seen = []
    l.for_each(lambda node, i: seen.append((node.data, i)))
    assert seen == [(1, 0), (2, 1), (3, 2)]

def test_iteration_with_for_loop():
    l = LinkedList()
    for x in ['x', 'y', 'z']:
        l.insert_last(x)
    assert [n.data for n in l] == ['x', 'y', 'z']

def test_append_same_as_insert_last():
    l = LinkedList()
    l.insert_last('a')
    l.append('b')
    l.append('c')
    assert l.size() == 3
    assert l.get_at(0).data == 'a'
    assert l.get_at(1).data == 'b'
    assert l.get_at(2).data == 'c'

def test_append_on_empty_list():
    l = LinkedList()
    l.append('first')
    assert l.get_first().data == 'first'
    assert l.size() == 1
