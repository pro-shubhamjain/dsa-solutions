/**
 * Problem: Circular Linked List
 * Pattern: Linked List (Floyd's cycle detection)
 * Time: O(n) | Space: O(1)
 *
 * Detect whether a linked list contains a cycle, using the classic
 * slow/fast ("tortoise and hare") pointer technique.
 *
 * Input:  a list where the last node's `next` points back into the list
 * Output: true
 */
function isCircularLinkList(list) {
    let slow = list.head;
    let fast = list.head;
    let isCque = false;
    while (fast.next && fast.next.next) {
      slow = slow.next;
      fast = fast.next.next;
      if (slow === fast) {
        isCque = true;
        return isCque;
      }
    }
    return isCque;
  }

  // Alternative: track visited nodes in a Set instead of Floyd's slow/fast
  // pointers. Time: O(n) same, but Space: O(n) instead of O(1) -- worth
  // knowing both since the Set version is easier to explain under pressure,
  // even though the two-pointer version is the "expected" optimal answer.
  function isCircularLinkListSet(list) {
    const visited = new Set();
    let current = list.head;
    while (current) {
      if (visited.has(current)) return true;
      visited.add(current);
      current = current.next;
    }
    return false;
  }

  module.exports = isCircularLinkList;
  module.exports.alternative = isCircularLinkListSet;