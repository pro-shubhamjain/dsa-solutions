// --- Directions
// Given a linked list, return the element n spaces
// from the last node in the list.  Do not call the 'size'
// method of the linked list.  Assume that n will always
// be less than the length of the list.
//
// Problem: Nth From Last
// Pattern: Linked List (two-pointer / runner technique)
// Time: O(n) | Space: O(1)
// --- Examples
//    const list = new List();
//    list.insertLast('a');
//    list.insertLast('b');
//    list.insertLast('c');
//    list.insertLast('d');
//    fromLast(list, 2).data // 'b'

function fromLast(list, n) {
    let slow = list.head;
    let fast = list.head;
  
    while (n > 0) {
      fast = fast.next;
      n--;
    }
  
    while (fast.next) {
      slow = slow.next;
      fast = fast.next;
    }
  
    return slow;
  }

  // Alternative: two-pass approach -- walk once to get the length, then walk
  // again to the target index. Same O(n) time, but two passes instead of one,
  // and it needs to know the length up front (the two-pointer version above
  // doesn't). Good to mention if the interviewer asks "can you do it in one pass?"
  function fromLastTwoPass(list, n) {
    let length = 0;
    let current = list.head;
    while (current) {
      length++;
      current = current.next;
    }

    const targetIndex = length - 1 - n;
    current = list.head;
    for (let i = 0; i < targetIndex; i++) {
      current = current.next;
    }
    return current;
  }
  
  module.exports = fromLast;
  module.exports.alternative = fromLastTwoPass;