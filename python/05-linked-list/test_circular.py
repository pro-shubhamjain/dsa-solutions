from linked_list import LinkedList
from circular import is_circular_linked_list, is_circular_linked_list_set

def test_non_circular_list():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    l.insert_last('c')
    assert is_circular_linked_list(l) is False

def test_circular_list():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    l.insert_last('c')
    # manually create a cycle: last node points back to head
    last = l.get_last()
    last.next = l.head
    assert is_circular_linked_list(l) is True

def test_alternative_matches():
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    assert is_circular_linked_list_set(l) is False
