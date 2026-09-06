from binary_search_tree import Node
from validate_bst import validate_bst, validate_bst_in_order

def test_valid_bst():
    root = Node(10)
    root.insert(5)
    root.insert(15)
    assert validate_bst(root) is True

def test_invalid_bst():
    root = Node(10)
    root.left = Node(15)   # deliberately wrong: left child > parent
    root.right = Node(5)
    assert validate_bst(root) is False

def test_in_order_alternative_matches():
    root = Node(10)
    root.insert(5)
    root.insert(15)
    assert validate_bst_in_order(root) is True
