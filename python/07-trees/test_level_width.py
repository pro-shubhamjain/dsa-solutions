from tree import TreeNode
from level_width import level_width, level_width_sentinel

def build_root():
    root = TreeNode('a')
    root.add('b')
    root.add('c')
    root.add('d')
    root.children[0].add('e')
    root.children[2].add('f')
    return root

def test_level_width():
    assert level_width(build_root()) == [1, 3, 2]

def test_level_width_sentinel_matches():
    assert level_width_sentinel(build_root()) == [1, 3, 2]
