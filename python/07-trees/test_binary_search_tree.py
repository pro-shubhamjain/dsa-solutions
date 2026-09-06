from binary_search_tree import Node, insert_iterative, contains_iterative

def test_insert_and_contains():
    root = Node(10)
    root.insert(5)
    root.insert(15)
    assert root.contains(5).data == 5
    assert root.contains(15).data == 15
    assert root.contains(100) is None

def test_insert_iterative_matches():
    root = Node(10)
    insert_iterative(root, 5)
    insert_iterative(root, 15)
    assert contains_iterative(root, 5).data == 5
    assert contains_iterative(root, 100) is None
