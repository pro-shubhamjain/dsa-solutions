/**
 * Problem: Stack
 * Pattern: Stacks & Queues
 * Time: O(1) push/pop/peek | Space: O(n)
 *
 * A stack is LIFO (Last In, First Out) -- the most recently pushed element
 * is the first one popped.
 *
 * Input:  s.push(1); s.push(2); s.push(3); s.pop(); s.pop(); s.pop();
 * Output: 3, 2, 1  (in that order)
 */
class Stack {
    constructor() {
      this.data = [];
    }
  
    push(record) {
      this.data.push(record);
    }
  
    pop() {
      return this.data.pop();
    }
  
    peek() {
      return this.data[this.data.length - 1];
    }
  }

  // Alternative: linked-list-backed stack instead of a JS array.
  // Same O(1) push/pop, but avoids relying on array's built-in push/pop --
  // useful to show you understand the underlying structure, not just Array API.
  class StackLinkedList {
    constructor() {
      this.top = null;
    }

    push(record) {
      this.top = { data: record, next: this.top };
    }

    pop() {
      if (!this.top) return undefined;
      const record = this.top.data;
      this.top = this.top.next;
      return record;
    }

    peek() {
      return this.top ? this.top.data : undefined;
    }
  }

  module.exports = Stack;
  module.exports.Alternative = StackLinkedList;