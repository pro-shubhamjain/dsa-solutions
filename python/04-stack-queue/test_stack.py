from stack import Stack, StackLinkedList

def test_stack_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_peek():
    s = Stack()
    s.push('a')
    s.push('b')
    assert s.peek() == 'b'
    assert s.pop() == 'b'
    assert s.peek() == 'a'

def test_stack_linked_list_behaves_the_same():
    s = StackLinkedList()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() is None
