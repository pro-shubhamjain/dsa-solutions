/**
 * Problem: Maximum Sum Subarray of Size K
 * Pattern: Sliding Window (fixed size)
 * Time: O(n) | Space: O(1)
 *
 * Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
 * Output: 9  (subarray [5, 1, 3])
 */

function maxSumSubarray(nums, k) {
    let windowSum = 0;
    for (let i = 0; i < k; i++) windowSum += nums[i];
    let maxSum = windowSum;

    for (let i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}

// Alternative: brute force -- recompute the sum of every window from
// scratch. Time: O(n*k) instead of O(n) -- included to make the sliding
// window's benefit concrete (this is what you'd naively write first,
// then optimize into the version above).
function maxSumSubarrayBruteForce(nums, k) {
    let maxSum = -Infinity;
    for (let i = 0; i <= nums.length - k; i++) {
        let windowSum = 0;
        for (let j = i; j < i + k; j++) {
            windowSum += nums[j];
        }
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}

console.log(maxSumSubarray([2, 1, 5, 1, 3, 2], 3)); // 9

module.exports = { maxSumSubarray, alternative: maxSumSubarrayBruteForce };
