/**
 * Problem: Factorial
 * Pattern: Fundamentals (recursion vs iteration)
 * Time: O(n) | Space: O(1) iterative, O(n) recursive (call stack)
 *
 * Compute n! = n * (n-1) * ... * 1, with 0! = 1! = 1.
 *
 * Input:  factorial(5)
 * Output: 120
 */
function factorial(n) {
    if (n < 0) {
      return "Factorial is not defined for negative numbers";
    }
    if (n === 0 || n === 1) {
      return 1;
    }
  
    return Array.from({length: n}, (_,index)=> index+1).reduce((a,b) => a*b, 1);
}

/**
 * BUG FOUND: factorialRecur claimed to be a recursive implementation but
 * called `factorial(n - 1)` (the iterative version above) instead of
 * `factorialRecur(n - 1)` -- so it only ever recursed one level deep before
 * handing off to the iterative version. Still produced correct results, but
 * didn't actually demonstrate recursion despite the name. Fixed to call
 * itself.
 */
function factorialRecur(n) {
  if (n === 0) {
      return 1;
  } else {
      return n * factorialRecur(n - 1);
  }
}

module.exports = {factorial, factorialRecur};