"""
Problem: Level Width
Pattern: Trees (breadth-first traversal)
Time: O(n) | Space: O(n)

Given the root of an n-ary tree, return a list where each entry is the
number of nodes at that depth (level) of the tree.

Input:  root 'a' with children 'b','c','d'; 'b' has child 'e'; 'd' has child 'f'
Output: [1, 3, 2]   -- 1 node at depth 0, 3 at depth 1, 2 at depth 2
"""

def level_width(root):
    queue = [root]
    counters = []
    while queue:
        counters.append(len(queue))
        next_level = []
        for node in queue:
            if getattr(node, 'children', None):
                next_level.extend(node.children)
        queue = next_level
    return counters


# Alternative: null-sentinel approach -- push a None marker after each
# level's nodes to know when one level ends and the next begins, instead of
# snapshotting the queue length up front. Same O(n) time; this is the more
# common textbook version of the null-sentinel BFS pattern.
def level_width_sentinel(root):
    arr = [root, None]
    counters = [0]
    while len(arr) > 1:
        node = arr.pop(0)
        if node is None:
            counters.append(0)
            arr.append(None)
        elif node is not None and hasattr(node, 'children'):
            # NOTE: must check `hasattr`, not truthiness of `node.children` --
            # an empty list is falsy in Python (unlike JS, where an empty
            # array is still truthy), so a truthiness check here silently
            # skipped leaf nodes and undercounted their level.
            arr.extend(node.children)
            counters[-1] += 1
    return counters


if __name__ == "__main__":
    from tree import TreeNode
    root = TreeNode('a')
    root.add('b')
    root.add('c')
    root.add('d')
    root.children[0].add('e')
    root.children[2].add('f')
    print(level_width(root))  # [1, 3, 2]
