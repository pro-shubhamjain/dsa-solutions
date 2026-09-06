from stack_queue import StackQueue

def test_stack_queue_fifo_order():
    q = StackQueue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3

def test_stack_queue_peek():
    q = StackQueue()
    q.add('a')
    q.add('b')
    assert q.peek() == 'a'
    assert q.remove() == 'a'
