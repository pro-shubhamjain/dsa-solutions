"""
Problem: Queue Implemented With Two Stacks
Pattern: Stacks & Queues
Time: amortized O(1) per operation (occasional O(n) shuffle between the two
      stacks) | Space: O(n)

Implement FIFO queue behavior using only two Stack instances (no list
pop(0)/insert(0)). Classic interview question testing whether you understand
how to simulate one structure with another.

Input:  q.add(1); q.add(2); q.add(3); q.remove(); q.remove(); q.remove()
Output: 1, 2, 3  (in that order, despite being backed by two LIFO stacks)
"""
from stack import Stack

class StackQueue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def add(self, n):
        self.first.push(n)

    def remove(self):
        while self.first.peek() is not None:
            self.second.push(self.first.pop())

        record = self.second.pop()

        while self.second.peek() is not None:
            self.first.push(self.second.pop())

        return record

    def peek(self):
        while self.first.peek() is not None:
            self.second.push(self.first.pop())

        record = self.second.peek()

        while self.second.peek() is not None:
            self.first.push(self.second.pop())

        return record


if __name__ == "__main__":
    q = StackQueue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q.remove())  # 1
