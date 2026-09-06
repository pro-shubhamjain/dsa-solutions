/**
 * Problem: Is Prime Number
 * Pattern: Fundamentals (trial division)
 * Time: O(sqrt(n)) | Space: O(1)
 *
 * Check whether a number is prime by testing divisibility up to its square root.
 *
 * Input:  isPrime(17)
 * Output: true
 */
function isPrime(number) {
    if (number <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
    return true;
  }

  // Alternative: 6k +/- 1 optimization -- after checking 2 and 3, every prime
  // is of the form 6k+1 or 6k-1, so we can skip straight to those candidates
  // instead of checking every integer up to sqrt(n). Same O(sqrt(n)) time
  // complexity class, but roughly 3x fewer iterations in practice.
  function isPrimeOptimized(number) {
    if (number <= 1) return false;
    if (number <= 3) return true;
    if (number % 2 === 0 || number % 3 === 0) return false;

    for (let i = 5; i * i <= number; i += 6) {
      if (number % i === 0 || number % (i + 2) === 0) return false;
    }
    return true;
  }
  
module.exports = isPrime;
module.exports.alternative = isPrimeOptimized;