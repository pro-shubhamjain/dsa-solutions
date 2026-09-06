// --- Directions
// 1) Implement the Node class to create
// a binary search tree.  The constructor
// should initialize values 'data', 'left',
// and 'right'.
// 2) Implement the 'insert' method for the
// Node class.  Insert should accept an argument
// 'data', then create an insert a new node
// at the appropriate location in the tree.
// 3) Implement the 'contains' method for the Node
// class.  Contains should accept a 'data' argument
// and return the Node in the tree with the same value.
// If the value isn't in the tree return null.
//
// Problem: Binary Search Tree
// Pattern: Trees
// Time: O(log n) average, O(n) worst case (unbalanced) | Space: O(1) per op
//
// Input:  const n = new Node(10); n.insert(5); n.insert(15); n.contains(5)
// Output: the Node with data === 5

class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }

  insert(data) {
    if (data < this.data && this.left) {
      this.left.insert(data);
    } else if (data < this.data) {
      this.left = new Node(data);
    } else if (data > this.data && this.right) {
      this.right.insert(data);
    } else if (data > this.data) {
      this.right = new Node(data);
    }
  }

  contains(data) {
    if (this.data === data) {
      return this;
    }

    if (this.data < data && this.right) {
      return this.right.contains(data);
    } else if (this.data > data && this.left) {
      return this.left.contains(data);
    }

    return null;
  }
}

// Alternative: iterative insert/contains instead of recursive.
// Same O(log n) average time, but avoids growing the call stack -- matters
// for very deep/unbalanced trees, and some interviewers specifically ask
// for the iterative version to check you're not just relying on recursion.
function insertIterative(root, data) {
  let current = root;
  while (true) {
    if (data < current.data) {
      if (!current.left) {
        current.left = new Node(data);
        return;
      }
      current = current.left;
    } else if (data > current.data) {
      if (!current.right) {
        current.right = new Node(data);
        return;
      }
      current = current.right;
    } else {
      return; // duplicate, no-op
    }
  }
}

function containsIterative(root, data) {
  let current = root;
  while (current) {
    if (current.data === data) return current;
    current = data < current.data ? current.left : current.right;
  }
  return null;
}

module.exports = Node;
module.exports.insertIterative = insertIterative;
module.exports.containsIterative = containsIterative;
