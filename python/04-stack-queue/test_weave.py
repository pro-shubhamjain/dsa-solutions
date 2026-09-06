from queue_ds import Queue
from weave import weave, weave_recursive

def make_queue(items):
    q = Queue()
    for item in items:
        q.add(item)
    return q

def drain(q):
    out = []
    while q.peek() is not None:
        out.append(q.remove())
    return out

def test_weave_alternates_elements():
    one = make_queue([1, 2, 3, 4])
    two = make_queue(['a', 'b', 'c', 'd'])
    result = weave(one, two)
    assert drain(result) == [1, 'a', 2, 'b', 3, 'c', 4, 'd']

def test_weave_recursive_matches():
    one = make_queue([1, 2])
    two = make_queue(['a', 'b'])
    result = weave_recursive(one, two)
    assert drain(result) == [1, 'a', 2, 'b']

def test_weave_handles_unequal_lengths():
    one = make_queue([1, 2, 3])
    two = make_queue(['a'])
    result = weave(one, two)
    assert drain(result) == [1, 'a', 2, 3]
