"""
Problem: Weave
Pattern: Stacks & Queues
Time: O(n) | Space: O(n)

Combine two queues by alternating their elements into a new queue.

Input:  one = Queue[1,2,3,4], two = Queue['a','b','c','d']
Output: Queue[1,'a',2,'b',3,'c',4,'d']
"""
from queue_ds import Queue


def weave(source_one, source_two):
    q = Queue()

    while source_one.peek() is not None or source_two.peek() is not None:
        if source_one.peek() is not None:
            q.add(source_one.remove())
        if source_two.peek() is not None:
            q.add(source_two.remove())

    return q


# Alternative: recursive instead of iterative. Same O(n) time, but uses the
# call stack instead of a while-loop.
def weave_recursive(source_one, source_two, q=None):
    if q is None:
        q = Queue()
    if source_one.peek() is None and source_two.peek() is None:
        return q
    if source_one.peek() is not None:
        q.add(source_one.remove())
    if source_two.peek() is not None:
        q.add(source_two.remove())
    return weave_recursive(source_one, source_two, q)


if __name__ == "__main__":
    from queue_ds import Queue as Q
    one, two = Q(), Q()
    for x in [1, 2, 3, 4]:
        one.add(x)
    for x in ['a', 'b', 'c', 'd']:
        two.add(x)
    result = weave(one, two)
    out = []
    while result.peek() is not None:
        out.append(result.remove())
    print(out)  # [1, 'a', 2, 'b', 3, 'c', 4, 'd']
