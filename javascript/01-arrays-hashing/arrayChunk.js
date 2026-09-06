/**
 * Problem: Array Chunk
 * Pattern: Arrays & Hashing (array slicing)
 * Time: O(n) | Space: O(n)
 *
 * Given an array and a chunk size, split it into subarrays of that length
 * (the last chunk may be shorter).
 *
 * Input:  chunk([1, 2, 3, 4, 5], 2)
 * Output: [[1, 2], [3, 4], [5]]
 */
function chunk(array, size) {
  const chunk = [];
  let index = 0;

  while (index < array.length) {
    chunk.push(array.slice(index, index + size));
    index += size;
  }
  
  return chunk;
}

// Alternative: build with reduce instead of a while-loop + slice.
// Same O(n) time, more functional style -- some interviewers like seeing both.
function chunkReduce(array, size) {
  return array.reduce((result, item, index) => {
    const chunkIndex = Math.floor(index / size);
    if (!result[chunkIndex]) result[chunkIndex] = [];
    result[chunkIndex].push(item);
    return result;
  }, []);
}

module.exports = chunk;
module.exports.alternative = chunkReduce;
