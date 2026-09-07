/**
 * Problem 1: Currying
 * Pattern: Fundamentals (closures / functional programming)
 * Time: O(1) | Space: O(1)
 *
 * Implement a curried calculator: calc() returns a chain of single-argument
 * functions -- add, sub, multi, divide -- each closing over the previous
 * argument, ending in getResult() which computes the final value.
 *
 * Input:  calc()(10)(5)(20)(2)()   i.e. (10 - 5) * 20 / 2
 * Output: 50
 */
function calc() {
  return function add(i1) {
    return function sub(i2) {
      return function multi(i3) {
        return function divide(i4) {
          return function getResult() {
            return (((i1 - i2) * i3) / i4);
          }
        }
      }
    }
  }
}

/**
 * Alternative: fluent/chainable API instead of currying.
 * Same idea (build up a computation step by step before reading the result)
 * but expressed as method chaining on a shared object instead of nested
 * function returns. This is the format some interviewers ask for explicitly
 * ("can you make it chainable instead of curried?").
 *
 * Input:  get().add(5).sub(2).multiply(10).divided(2).getResult()
 * Output: 15   i.e. ((0 + 5 - 2) * 10) / 2
 */
function get() {
  let value = 0;

  const api = {
    add: function (num) {
      value += num;
      return api;
    },
    sub: function (num) {
      value -= num;
      return api;
    },
    multiply: function (num) {
      value *= num;
      return api;
    },
    divided: function (num) {
      if (num !== 0) {
        value /= num;
      } else {
        console.error("Cannot divide by zero.");
      }
      return api;
    },
    getResult: function () {
      return value;
    },
  };

  return api;
}

/**
 * Problem 2: Closures and `var` in a loop (the classic gotcha -- and why
 * this particular code actually avoids it)
 * Pattern: Fundamentals (closures / scoping)
 *
 * The textbook version of this bug is:
 *   for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 1); }
 * which logs 3, 3, 3 -- because the arrow function closes directly over the
 * loop's single shared `var i` binding, and by the time the callbacks run,
 * the loop has already finished with i === 3.
 *
 * This file's version passes `i` as an ARGUMENT to print(i) instead of
 * closing over the loop variable directly. Each call to print() creates its
 * own fresh `i` parameter, so the closure inside setTimeout captures that
 * per-call parameter, not the loop's shared variable. That's a common
 * pre-`let` workaround (wrap the loop body in a function call), so this
 * code actually prints the values correctly despite using `var`.
 *
 * Input:  closure()
 * Output (after ~1ms, printed via console.log): 0, 1, 2
 */
function print(i) {
    setTimeout(() => {
     console.log(i);
    }, 1);
}

function closure() {
  for(let i = 0 ; i<3; i++) {
    print(i);
  }
}

/**
 * Alternative: the modern equivalent using `let`. `let` is block-scoped, so
 * each loop iteration already gets its own binding of `i` -- no need for
 * the print()-as-wrapper trick above. Given directly as an inline arrow
 * function (no separate print() call needed) to show the more common
 * modern style.
 *
 * Input:  closureFixed()
 * Output (after ~1ms, printed via console.log): 0, 1, 2
 */
function closureFixed() {
  for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 1);
  }
}

module.exports = {
  calc,
  alternative: get,
  closure,
  closureFixed,
}
