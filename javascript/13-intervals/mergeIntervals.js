/**
 * Problem: Merge Intervals
 * Pattern: Intervals (sort + sweep)
 * Time: O(n log n) | Space: O(n)
 *
 * Given a list of [start, end] intervals, merge all overlapping ones.
 *
 * Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
 * Output: [[1, 6], [8, 10], [15, 18]]
 */
function mergeIntervals(intervals) {
  if (intervals.length === 0) return [];
  intervals.sort((a, b) => a[0] - b[0]);
  const mergedInterval = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const currentInterval = intervals[i];
    const previousInterval = mergedInterval[mergedInterval.length - 1];
    if (currentInterval[0] <= previousInterval[1]) {
      previousInterval[1] = Math.max(currentInterval[1], previousInterval[1]);
    } else {
      mergedInterval.push(currentInterval);
    }
  }

  return mergedInterval;
}

// Alternative: recursive merge instead of an iterative loop.
// Same O(n log n) time (dominated by the sort), just a different control flow.
function mergeIntervalsRecursive(intervals) {
  if (intervals.length === 0) return [];
  const sorted = [...intervals].sort((a, b) => a[0] - b[0]);

  function mergeFrom(index, acc) {
    if (index === sorted.length) return acc;
    const current = sorted[index];
    const last = acc[acc.length - 1];
    if (last && current[0] <= last[1]) {
      last[1] = Math.max(last[1], current[1]);
    } else {
      acc.push([...current]);
    }
    return mergeFrom(index + 1, acc);
  }

  return mergeFrom(0, []);
}

module.exports =  mergeIntervals;
module.exports.alternative = mergeIntervalsRecursive;
