
// --- Directions
// Given a node, validate the binary search tree,
// ensuring that every node's left hand child is
// less than the parent node's value, and that
// every node's right hand child is greater than
// the parent
//
// Problem: Validate Binary Search Tree
// Pattern: Trees (recursive range checking)
// Time: O(n) | Space: O(h) call stack, h = tree height
//
// Input:  a BST-shaped tree with one node out of order
// Output: false

function validateBST(node, min = null, max = null) {
    if (max !== null && node.data > max) {
      return false;
    }
  
    if (min !== null && node.data < min) {
      return false;
    }
  
    if (node.left && !validateBST(node.left, min, node.data)) {
      return false;
    }
  
    if (node.right && !validateBST(node.right, node.data, max)) {
      return false;
    }
  
    return true;
  }

  // Alternative: in-order traversal must produce a strictly increasing
  // sequence for a valid BST. Same O(n) time, but Space: O(n) for the
  // collected values array vs O(h) call-stack space for the range-check
  // version above (h = tree height). Conceptually simpler to explain.
  function validateBSTInOrder(node) {
    const values = [];
    (function inOrder(n) {
      if (!n) return;
      inOrder(n.left);
      values.push(n.data);
      inOrder(n.right);
    })(node);

    for (let i = 1; i < values.length; i++) {
      if (values[i] <= values[i - 1]) return false;
    }
    return true;
  }
  
  module.exports = validateBST;
  module.exports.alternative = validateBSTInOrder;
  