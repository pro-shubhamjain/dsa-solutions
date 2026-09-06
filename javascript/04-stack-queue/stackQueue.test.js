const StackQueue = require('./stackQueue');

test('StackQueue is a class', () => {
  expect(typeof StackQueue.prototype.constructor).toEqual('function');
});

test('behaves like a queue (FIFO) even though built from two stacks', () => {
  const q = new StackQueue();
  q.add(1);
  q.add(2);
  q.add(3);
  expect(q.remove()).toEqual(1);
  expect(q.remove()).toEqual(2);
  expect(q.remove()).toEqual(3);
});

test('peek returns the next item without removing it', () => {
  const q = new StackQueue();
  q.add('a');
  q.add('b');
  expect(q.peek()).toEqual('a');
  expect(q.remove()).toEqual('a');
  expect(q.peek()).toEqual('b');
});
