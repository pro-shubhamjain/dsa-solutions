"""
Problem: Singly Linked List
Pattern: Linked List
Time: varies per method (see below) | Space: O(n)

A full singly-linked-list implementation: insert/remove at either end or an
arbitrary index, size, and iteration.

Input:  l.insert_last('a'); l.insert_last('b'); l.get_at(1).data
Output: 'b'
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter

    def get_first(self):
        return self.head

    def get_last(self):
        if not self.head:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node

    def clear(self):
        self.head = None

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        previous = self.head
        node = self.head.next
        while node.next:
            previous = node
            node = node.next
        previous.next = None

    def insert_last(self, data):
        last = self.get_last()
        if last:
            last.next = Node(data)
        else:
            self.head = Node(data)

    def get_at(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.next
        return None

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        previous = self.get_at(index - 1)
        if not previous or not previous.next:
            return
        previous.next = previous.next.next

    def insert_at(self, data, index):
        if not self.head:
            self.head = Node(data)
            return
        if index == 0:
            self.head = Node(data, self.head)
            return
        previous = self.get_at(index - 1) or self.get_last()
        node = Node(data, previous.next)
        previous.next = node

    def for_each(self, fn):
        node = self.head
        counter = 0
        while node:
            fn(node, counter)
            node = node.next
            counter += 1

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


if __name__ == "__main__":
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    print(l.get_at(1).data)  # b
