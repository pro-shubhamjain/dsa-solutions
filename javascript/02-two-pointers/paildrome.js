/**
 * Problem: Palindrome
 * Pattern: Two Pointers (string comparison)
 * Time: O(n) | Space: O(n)
 *
 * Check whether a string reads the same forwards and backwards.
 * Case-sensitive and whitespace-sensitive (no normalization applied).
 *
 * Input:  palindrome('aba')
 * Output: true
 */
function palindrome(string) {
   const reverseString = string.split('').reverse().join('');
   return string === reverseString;
}

// Alternative: two-pointer comparison, no extra reversed string built.
// Time: O(n) same, but Space: O(1) instead of O(n) -- genuinely better.
function palindromeTwoPointer(string) {
  let left = 0, right = string.length - 1;
  while (left < right) {
    if (string[left] !== string[right]) return false;
    left++;
    right--;
  }
  return true;
}

module.exports = palindrome;
module.exports.alternative = palindromeTwoPointer;