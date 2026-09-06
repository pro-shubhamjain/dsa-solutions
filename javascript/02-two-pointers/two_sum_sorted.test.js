const { twoSum } = require('./two_sum_sorted');

test('twoSum is a function', () => {
  expect(typeof twoSum).toEqual('function');
});

test('finds indices of two numbers that sum to target', () => {
  expect(twoSum([1, 2, 4, 6, 8, 9], 11)).toEqual([1, 5]);
});

test('returns empty array when no pair sums to target', () => {
  expect(twoSum([1, 2, 3], 100)).toEqual([]);
});

test('alternative (hash map) gives the same result on an unsorted array', () => {
  const { alternative } = require('./two_sum_sorted');
  expect(alternative([4, 1, 9, 6, 2, 8], 11)).toEqual([2, 4]); // nums[2] + nums[4] = 9 + 2 = 11
});
