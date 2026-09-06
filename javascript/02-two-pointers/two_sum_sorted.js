/**
 * Problem: Two Sum II - Input Array Is Sorted
 * Pattern: Two Pointers
 * Time: O(n) | Space: O(1)
 *
 * Input:  nums = [1, 2, 4, 6, 8, 9], target = 11
 * Output: [1, 5]  (nums[1] + nums[5] = 2 + 9 = 11)
 */

function twoSum(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        const currSum = nums[left] + nums[right];
        if (currSum === target) {
            return [left, right];
        } else if (currSum < target) {
            left++;
        } else {
            right--;
        }
    }
    return [];
}

// Alternative: hash map lookup instead of two pointers. Same O(n) time and
// O(n) space instead of O(1) -- but this version does NOT require the array
// to be sorted, so it's the more general approach (this is the classic
// "Two Sum I" solution). Good to know both: two-pointer when sorted +
// O(1) space matters, hash map when the array isn't sorted.
function twoSumHashMap(nums, target) {
    const seen = new Map(); // value -> index
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(nums[i], i);
    }
    return [];
}

console.log(twoSum([1, 2, 4, 6, 8, 9], 11)); // [1, 5]

module.exports = { twoSum, alternative: twoSumHashMap };
