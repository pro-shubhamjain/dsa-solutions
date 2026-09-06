/**
 * Problem: Level Width
 * Pattern: Trees (breadth-first traversal)
 * Time: O(n) | Space: O(n)
 *
 * Given the root of an n-ary tree, return an array where each entry is the
 * number of nodes at that depth (level) of the tree.
 *
 * Input:  root 'a' with children 'b','c','d'; 'b' has child 'e'; 'd' has child 'f'
 * Output: [1, 3, 2]   -- 1 node at depth 0, 3 at depth 1, 2 at depth 2
 */
function levelWidth(root) {
  const arr = [root, null]; // Use null as the sentinel value
  const counters = [0];

  while (arr.length > 1) {
    const node = arr.shift();

    if (node === null) {
      counters.push(0);
      arr.push(null); // Push the sentinel value
    } else if (node && node.children) {
      arr.push(...node.children);
      counters[counters.length - 1]++;
    }
  }

  return counters;
}

// Alternative: standard level-order BFS that snapshots the queue length at
// the start of each level, instead of using a null sentinel to mark level
// boundaries. Same O(n) time -- this version is the more common pattern
// you'll see in general tree/graph BFS problems, so worth knowing both.
function levelWidthQueueSnapshot(root) {
  const counters = [];
  let queue = [root];

  while (queue.length) {
    counters.push(queue.length);
    const next = [];
    for (const node of queue) {
      if (node.children) next.push(...node.children);
    }
    queue = next;
  }

  return counters;
}

module.exports = levelWidth;
module.exports.alternative = levelWidthQueueSnapshot;