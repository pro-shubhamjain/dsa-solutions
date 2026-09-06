/**
 * Problem: Queue
 * Pattern: Stacks & Queues
 * Time: add O(n) / remove O(1) for the array version below (see Alternative
 *       for a true O(1)/O(1) version) | Space: O(n)
 *
 * A queue is FIFO (First In, First Out) -- the first element added is the
 * first one removed. (Not to be confused with a Stack, which is LIFO.)
 *
 * Input:  q.add(1); q.add(2); q.add(3); q.remove(); q.remove(); q.remove();
 * Output: 1, 2, 3  (in that order)
 */
class Queue {
  constructor() {
    this.data = [];
  }

  add(n) {
     this.data.unshift(n);
  }

  remove() {
    return this.data.pop();
  }

  peek() {
    return this.data[this.data.length - 1];
  }

  QueueList() {
    return this.data;
  }
}

// Alternative: linked-list-backed queue with head/tail pointers.
// The array version above does `unshift` on add, which is O(n) (shifts every
// element). This version gets add/remove down to true O(1).
class QueueLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  add(n) {
    const node = { data: n, next: null };
    if (this.tail) {
      this.tail.next = node;
    } else {
      this.head = node;
    }
    this.tail = node;
  }

  remove() {
    if (!this.head) return undefined;
    const record = this.head.data;
    this.head = this.head.next;
    if (!this.head) this.tail = null;
    return record;
  }

  peek() {
    return this.head ? this.head.data : undefined;
  }
}

module.exports = Queue;
module.exports.Alternative = QueueLinkedList;