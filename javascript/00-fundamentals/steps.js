/**
 * Problem: Steps / Staircase Patterns
 * Pattern: Fundamentals (nested loops, string building)
 * Time: O(n^2) | Space: O(n) per printed row
 *
 * Print an n-row staircase of '#' characters, in various orientations.
 * Four variants below build the same basic shape from different corners.
 *
 * Input:  steps(3)
 * Output (via console.log, one row per line):
 *   #
 *   ##
 *   ###
 */
function steps(n) {
  for (let row = 0; row < n; row++) {
    let stair = '';

    for (let column = 0; column < n; column++) {
      if (column <= row) {
        stair += '#';
      } else {
        stair += ' ';
      }
    }

    console.log(stair);
  }
}

/**
 * stepsRTL: staircase built right-to-left -- each row is right-padded with
 * spaces so the '#' block is flush against the right edge, growing upward.
 *
 * Input:  stepsRTL(3)
 * Output:
 *     #
 *    ##
 *   ###
 */
function stepsRTL(input) {
    for (let row = input - 1; row >= 0; row--) {
      let level = '';
      for (let col = 0; col < input; col++) {
        if (col >= row) {
          level += '#';
        } else {
          level += ' ';
        }
      }
      console.log(level);
    }
  }

/**
 * stepsLTR: ascending staircase, left-aligned, no trailing spaces --
 * row 0 has 1 '#', row 1 has 2, ..., row (n-1) has n.
 *
 * BUG FOUND: the original loop was `for (let col = row; col > 0; col--)`,
 * which prints `row` hashes per row instead of `row + 1` -- so row 0 printed
 * ZERO hashes (a blank line) instead of one. Verified by running it:
 * stepsLTR(3) produced ['', '#', '##'] instead of ['#', '##', '###'].
 * Fixed by counting from 1 to row+1 instead of from row down to 1.
 *
 * Input:  stepsLTR(3)
 * Output:
 *   #
 *   ##
 *   ###
 */
  function stepsLTR(input) {
    for (let row = 0; row < input; row++) {
      let level = '';
      for (let col = 0; col <= row; col++) {
          level += '#';
      }
       console.log(level);
    }
  }

/**
 * downToTop: descending staircase, left-aligned -- row 0 has n hashes,
 * shrinking down to 1 hash on the last row (the mirror image of stepsLTR).
 * Despite the name, it prints widest-row-first; "downToTop" refers to the
 * shrinking direction of the pattern, not the print order.
 *
 * Input:  downToTop(3)
 * Output:
 *   ###
 *   ##
 *   #
 */
  function downToTop(input) {
     for (let row = 0; row < input; row++) {
       let level = '';
       for (let col = row; col < input; col++) {
           level += '#';
       }
        console.log(level);
     }
  }

module.exports = { 
  stepsRTL,
  stepsLTR,
  downToTop,
  steps
}
