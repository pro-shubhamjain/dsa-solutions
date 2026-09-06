"""
Problem: Validate Binary Search Tree
Pattern: Trees (recursive range checking)
Time: O(n) | Space: O(h) call stack, h = tree height

Given a node, validate that it's a proper binary search tree -- every left
child is less than its parent, every right child is greater.

Input:  a BST-shaped tree with one node out of order
Output: False
"""

def validate_bst(node, min_val=None, max_val=None):
    if max_val is not None and node.data > max_val:
        return False
    if min_val is not None and node.data < min_val:
        return False
    if node.left and not validate_bst(node.left, min_val, node.data):
        return False
    if node.right and not validate_bst(node.right, node.data, max_val):
        return False
    return True


# Alternative: in-order traversal must produce a strictly increasing
# sequence for a valid BST. Same O(n) time, but O(n) space for the
# collected values vs O(h) call-stack space for the range-check version.
def validate_bst_in_order(node):
    values = []

    def in_order(n):
        if not n:
            return
        in_order(n.left)
        values.append(n.data)
        in_order(n.right)

    in_order(node)
    return all(values[i] > values[i - 1] for i in range(1, len(values)))


if __name__ == "__main__":
    from binary_search_tree import Node
    root = Node(10)
    root.insert(5)
    root.insert(15)
    print(validate_bst(root))  # True
