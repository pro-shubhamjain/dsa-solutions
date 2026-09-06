/**
 * Problem: Weave
 * Pattern: Stacks & Queues
 * Time: O(n) | Space: O(n)
 *
 * Combine two queues by alternating their elements into a new queue.
 *
 * Input:  one = Queue[1,2,3,4], two = Queue['a','b','c','d']
 * Output: Queue[1,'a',2,'b',3,'c',4,'d']
 */
const Queue = require('./queue');

function weave(sourceOne, sourceTwo) {
  const q = new Queue;
  
  // Continue looping until both sourceOne and sourceTwo are empty
  while (sourceOne.peek() || sourceTwo.peek()) {
    if (sourceOne.peek()) {
      q.add(sourceOne.remove());
    }

    if (sourceTwo.peek()) {
      q.add(sourceTwo.remove());
    }
  }

  // Return the result as an array with alternating elements
  return q;
}

// Alternative: recursive instead of iterative. Same O(n) time, but uses the
// call stack instead of a while-loop -- worth knowing both since interviewers
// sometimes ask for a recursive version specifically.
function weaveRecursive(sourceOne, sourceTwo, q = new Queue()) {
  if (!sourceOne.peek() && !sourceTwo.peek()) return q;
  if (sourceOne.peek()) q.add(sourceOne.remove());
  if (sourceTwo.peek()) q.add(sourceTwo.remove());
  return weaveRecursive(sourceOne, sourceTwo, q);
}

module.exports = weave;
module.exports.alternative = weaveRecursive;
