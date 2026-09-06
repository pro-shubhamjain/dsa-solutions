"""
Problem: Binary Search Tree
Pattern: Trees
Time: O(log n) average, O(n) worst case (unbalanced) | Space: O(1) per op

Implement a Node class for a binary search tree: insert(data) places a new
node in the correct position, contains(data) finds a node with that value.

Input:  n = Node(10); n.insert(5); n.insert(15); n.contains(5)
Output: the Node with data == 5
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data and self.left:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        elif data > self.data:
            self.right = Node(data)

    def contains(self, data):
        if self.data == data:
            return self
        if self.data < data and self.right:
            return self.right.contains(data)
        elif self.data > data and self.left:
            return self.left.contains(data)
        return None


# Alternative: iterative insert/contains instead of recursive.
# Same O(log n) average time, avoids growing the call stack.
def insert_iterative(root, data):
    current = root
    while True:
        if data < current.data:
            if not current.left:
                current.left = Node(data)
                return
            current = current.left
        elif data > current.data:
            if not current.right:
                current.right = Node(data)
                return
            current = current.right
        else:
            return  # duplicate, no-op


def contains_iterative(root, data):
    current = root
    while current:
        if current.data == data:
            return current
        current = current.left if data < current.data else current.right
    return None


if __name__ == "__main__":
    root = Node(10)
    root.insert(5)
    root.insert(15)
    print(root.contains(5).data)  # 5
