/**
 * Problem: Count Vowels
 * Pattern: Arrays & Hashing (string scanning)
 * Time: O(n) | Space: O(1)
 *
 * Count how many vowels (a, e, i, o, u -- case-insensitive) appear in a string.
 *
 * Input:  countVowels('aeiou')
 * Output: 5
 */
function countVowelsType1(string) {
    const vowel= ['a','e','i','o','u'];
    return  string.split('').filter(e => vowel.includes(e)).length;
 }

function countVowels(string) {
   const matchString = string.toLowerCase().match(/[aeiou]/gi);
   return  matchString ? matchString.length : 0;
}

module.exports = countVowels;
module.exports.alternative = countVowelsType1; // approach 2: filter + includes, O(n) same complexity, less efficient in practice (array allocation)

