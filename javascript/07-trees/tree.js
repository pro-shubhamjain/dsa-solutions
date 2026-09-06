/**
 * Problem: N-ary Tree (add/remove children, BFS/DFS traversal)
 * Pattern: Trees
 * Time: O(n) for traversal methods | Space: O(n)
 *
 * TreeNode: a node that can hold any number of children (not binary).
 * Tree: wraps a root TreeNode and provides breadth-first and depth-first
 * traversal, each taking a callback invoked once per visited node.
 *
 * Input:  tree with root 'a', children 'b' and 'd', and 'b' has child 'c'
 * Output: traverseBF visits a, b, d, c (level by level)
 *         traverseDF visits a, b, c, d (depth-first, left branch fully first)
 */
class TreeNode {
    constructor(data) {
      this.data = data;
      this.children = [];
    }
  
    add(data) {
      this.children.push(new TreeNode(data));
    }
  
    remove(data) {
      this.children = this.children.filter((node) => {
        return node.data !== data;
      });
    }
  }
  
  class Tree {
    constructor() {
      this.root = null;
    }
  
    traverseBF(fn) {
      const arr = [this.root];
      while (arr.length) {
        const node = arr.shift();
        arr.push(...node.children);
        fn(node);
      }
    }
  
    traverseDF(fn) {
      const arr = [this.root];
      while (arr.length) {
        const node = arr.shift();
        arr.unshift(...node.children);
        fn(node);
      }
    }
  }

  module.exports = {Tree, TreeNode};