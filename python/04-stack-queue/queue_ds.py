"""
Problem: Queue
Pattern: Stacks & Queues
Time: add O(1) / remove O(n) for the list version below (Python's list.pop(0)
      shifts every element) | Space: O(n)

A queue is FIFO (First In, First Out) -- the first element added is the
first one removed. (Not to be confused with a Stack, which is LIFO.)

Input:  q.add(1); q.add(2); q.add(3); q.remove(); q.remove(); q.remove()
Output: 1, 2, 3  (in that order)
"""

class Queue:
    def __init__(self):
        self.data = []

    def add(self, n):
        self.data.append(n)

    def remove(self):
        return self.data.pop(0) if self.data else None

    def peek(self):
        return self.data[0] if self.data else None


# Alternative: linked-list-backed queue with head/tail pointers.
# The list version above does list.pop(0) on remove, which is O(n) (shifts
# every remaining element). This version gets add/remove down to true O(1).
class QueueLinkedList:
    class _Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, n):
        node = self._Node(n)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def remove(self):
        if not self.head:
            return None
        record = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return record

    def peek(self):
        return self.head.data if self.head else None


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    print(q.remove())  # 1
