const mergeIntervals = require('./mergeIntervals');

test('mergeIntervals is a function', () => {
  expect(typeof mergeIntervals).toEqual('function');
});

test('merges overlapping intervals', () => {
  expect(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]])).toEqual([
    [1, 6],
    [8, 10],
    [15, 18],
  ]);
});

test('merges intervals that touch at the boundary', () => {
  expect(mergeIntervals([[1, 4], [4, 5]])).toEqual([[1, 5]]);
});

test('leaves non-overlapping intervals unchanged', () => {
  expect(mergeIntervals([[1, 2], [3, 4]])).toEqual([[1, 2], [3, 4]]);
});

test('returns [] for empty input', () => {
  expect(mergeIntervals([])).toEqual([]);
});
