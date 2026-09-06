/**
 * Problem: Anagrams
 * Pattern: Arrays & Hashing (string normalization)
 * Time: O(n log n) | Space: O(n)
 *
 * Check whether two strings are anagrams of each other -- same characters,
 * same quantities, ignoring case, spaces, and punctuation.
 *
 * Input:  anagrams('hello', 'llohe')
 * Output: true
 */
function anagrams(stringA, stringB) {
  const flag = cleanString(stringA) == cleanString(stringB);
  return flag;
}

function cleanString(string) {
  return string.replace(/[^\w]/g, '').toLowerCase().split('').sort().join('');
}

// Alternative: character-frequency map comparison instead of sorting.
// Time: O(n) instead of O(n log n) -- genuinely better, good to mention.
function anagramsFrequencyMap(stringA, stringB) {
  const countA = buildCharMap(stringA);
  const countB = buildCharMap(stringB);

  if (Object.keys(countA).length !== Object.keys(countB).length) return false;
  for (const char in countA) {
    if (countA[char] !== countB[char]) return false;
  }
  return true;
}

function buildCharMap(string) {
  const map = {};
  for (const char of string.replace(/[^\w]/g, '').toLowerCase()) {
    map[char] = (map[char] || 0) + 1;
  }
  return map;
}

module.exports = anagrams;
module.exports.alternative = anagramsFrequencyMap;

