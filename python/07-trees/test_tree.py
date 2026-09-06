from tree import Tree, TreeNode

def build_tree():
    t = Tree()
    t.root = TreeNode('a')
    t.root.add('b')
    t.root.add('d')
    t.root.children[0].add('c')
    return t

def test_traverse_bf():
    t = build_tree()
    visited = []
    t.traverse_bf(lambda n: visited.append(n.data))
    assert visited == ['a', 'b', 'd', 'c']

def test_traverse_df():
    t = build_tree()
    visited = []
    t.traverse_df(lambda n: visited.append(n.data))
    assert visited == ['a', 'b', 'c', 'd']

def test_remove_child():
    root = TreeNode('a')
    root.add('b')
    root.add('c')
    root.remove('b')
    assert [c.data for c in root.children] == ['c']
