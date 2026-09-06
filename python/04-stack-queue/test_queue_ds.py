from queue_ds import Queue, QueueLinkedList

def test_queue_fifo_order():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3

def test_queue_peek():
    q = Queue()
    q.add('a')
    q.add('b')
    assert q.peek() == 'a'
    assert q.remove() == 'a'
    assert q.peek() == 'b'

def test_queue_linked_list_behaves_the_same():
    q = QueueLinkedList()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3
