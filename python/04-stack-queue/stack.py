"""
Problem: Stack
Pattern: Stacks & Queues
Time: O(1) push/pop/peek | Space: O(n)

A stack is LIFO (Last In, First Out) -- the most recently pushed element
is the first one popped.

Input:  s.push(1); s.push(2); s.push(3); s.pop(); s.pop(); s.pop()
Output: 3, 2, 1  (in that order)
"""

class Stack:
    def __init__(self):
        self.data = []

    def push(self, record):
        self.data.append(record)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None


# Alternative: linked-list-backed stack instead of a Python list.
# Same O(1) push/pop, but avoids relying on list's built-in append/pop --
# shows you understand the underlying structure, not just the list API.
class StackLinkedList:
    class _Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.top = None

    def push(self, record):
        self.top = self._Node(record, self.top)

    def pop(self):
        if not self.top:
            return None
        record = self.top.data
        self.top = self.top.next
        return record

    def peek(self):
        return self.top.data if self.top else None


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())  # 2
