const { maxSumSubarray } = require('./max_sum_subarray');

test('maxSumSubarray is a function', () => {
  expect(typeof maxSumSubarray).toEqual('function');
});

test('finds the max sum of a window of size k', () => {
  expect(maxSumSubarray([2, 1, 5, 1, 3, 2], 3)).toEqual(9);
});

test('works when k equals array length', () => {
  expect(maxSumSubarray([1, 2, 3], 3)).toEqual(6);
});

test('alternative (brute force) gives the same result', () => {
  const { alternative } = require('./max_sum_subarray');
  expect(alternative([2, 1, 5, 1, 3, 2], 3)).toEqual(9);
});
