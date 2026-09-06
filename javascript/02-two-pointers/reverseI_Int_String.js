/**
 * Problem: Reverse String and Integer
 * Pattern: Two Pointers (string/number reversal)
 * Time: O(n) | Space: O(n)
 *
 * reverseString: reverse the characters of a string.
 * reverseInteger: reverse the digits of an integer, preserving its sign.
 *
 * Input:  reverseString('abcd')
 * Output: 'dcba'
 *
 * Input:  reverseInteger(-2359)
 * Output: -9532
 */
function reverseString(string) {
  const revStr = string?.split('')?.reverse()?.join('');
  return revStr;
}

function reverseInteger(input) {
  const convertNumber = Math.floor(input).toString().split('').reverse().join('');
  return parseInt(convertNumber) * Math.sign(input)
}

module.exports = { reverseString, reverseInteger};