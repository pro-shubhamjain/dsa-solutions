/**
 * Problem: FizzBuzz
 * Pattern: Fundamentals (conditionals, modulo)
 * Time: O(n) | Space: O(n) for the array version, O(1) for the print version
 *
 * For each number 1..n: print/collect "fizz" if divisible by 3, "buzz" if
 * divisible by 5, "fizzbuzz" if divisible by both, otherwise the number itself.
 *
 * Input:  fizzBuzzArray(5)
 * Output: [1, 2, 'fizz', 4, 'buzz']
 */

/**
 * BUG FOUND: this function's own output strings had typos -- 'fiz' and
 * 'fizbuzz' instead of 'fizz' and 'fizzbuzz' (missing a 'z' both times).
 * It also wasn't covered by any test, which is exactly how a typo like this
 * survives. Fixed the strings and renamed from `fizbuzz` to `fizzBuzzArray`
 * for consistency with the spelling everywhere else in the codebase.
 */
function fizzBuzzArray(input) {
    if(input <  1 ) return input;
    const filledArray = Array.from({ length: input }, (_, index) => index+1);
  
    let fizzBuzzMap = filledArray.map((e) => {
        const fizz = e % 3 == 0;
        const buzz = e % 5 == 0;
        return ( fizz && buzz ) ? 'fizzbuzz' : fizz ? 'fizz' : buzz ? 'buzz' : e;
    });
  
    return fizzBuzzMap;
}

/**
 * Alternative: prints each value via console.log instead of returning an
 * array. Same O(n) time and logic, different output mechanism -- some
 * interviewers ask for the print version specifically, others want the
 * array returned so it's testable without mocking console.log.
 *
 * Input:  fizzBuzz1(5)
 * Output (via console.log): 1, 2, 'fizz', 4, 'buzz'
 */
function fizzBuzz1(n) {
  for (let i = 1; i <= n; i++) {
    // Is the number a multiple of 3 and 5?
    if (i % 3 === 0 && i % 5 === 0) {
      console.log('fizzbuzz');
    } else if (i % 3 === 0) {
      // Is the number a multiple of 3?
      console.log('fizz');
    } else if (i % 5 === 0) {
      console.log('buzz');
    } else {
      console.log(i);
    }
  }
}

module.exports = { fizzBuzzArray, fizzBuzz1 };
