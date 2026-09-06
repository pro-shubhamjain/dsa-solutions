/**
 * Problem: Queue Implemented With Two Stacks
 * Pattern: Stacks & Queues
 * Time: amortized O(1) per operation (occasional O(n) shuffle between the
 *       two stacks) | Space: O(n)
 *
 * Implement FIFO queue behavior using only two Stack instances (no array
 * shift/unshift). Classic interview question testing whether you understand
 * how to simulate one structure with another.
 *
 * Input:  q.add(1); q.add(2); q.add(3); q.remove(); q.remove(); q.remove();
 * Output: 1, 2, 3  (in that order, despite being backed by two LIFO stacks)
 */
const Stack = require('./stack');

class stackQueue {
  constructor() {
    this.first = new Stack();
    this.second = new Stack();
  }

  add(n) {
    this.first.push(n);
  }

  remove() {
    while (this.first.peek()) {
      this.second.push(this.first.pop());
    }

    const record = this.second.pop();

    while (this.second.peek()) {
      this.first.push(this.second.pop());
    }

    return record;
  }

  peek() {
    while (this.first.peek()) {
      this.second.push(this.first.pop());
    }
    const record = this.second.peek();

    while (this.second.peek()) {
      this.first.push(this.second.pop());
    }

    return record;
  }
}
module.exports = stackQueue;