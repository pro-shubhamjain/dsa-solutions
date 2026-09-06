"""
Problem: N-ary Tree (add/remove children, BFS/DFS traversal)
Pattern: Trees
Time: O(n) for traversal methods | Space: O(n)

TreeNode: a node that can hold any number of children (not binary).
Tree: wraps a root TreeNode and provides breadth-first and depth-first
traversal, each taking a callback invoked once per visited node.

Input:  tree with root 'a', children 'b' and 'd', and 'b' has child 'c'
Output: traverse_bf visits a, b, d, c (level by level)
        traverse_df visits a, b, c, d (depth-first, left branch fully first)
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(TreeNode(data))

    def remove(self, data):
        self.children = [node for node in self.children if node.data != data]


class Tree:
    def __init__(self):
        self.root = None

    def traverse_bf(self, fn):
        arr = [self.root]
        while arr:
            node = arr.pop(0)
            arr.extend(node.children)
            fn(node)

    def traverse_df(self, fn):
        arr = [self.root]
        while arr:
            node = arr.pop(0)
            arr[0:0] = node.children  # prepend children (mirrors JS unshift)
            fn(node)


if __name__ == "__main__":
    t = Tree()
    t.root = TreeNode('a')
    t.root.add('b')
    t.root.add('d')
    t.root.children[0].add('c')
    visited = []
    t.traverse_df(lambda n: visited.append(n.data))
    print(visited)  # ['a', 'b', 'c', 'd']
