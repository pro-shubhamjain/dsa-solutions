/**
 * Problem: Pyramid
 * Pattern: Fundamentals (nested loops, string building)
 * Time: O(n^2) | Space: O(n) per printed row
 *
 * Print a centered pyramid of '#' characters, n rows tall.
 *
 * Input:  pyramid(3)
 * Output (via console.log):
 *     #
 *    ###
 *   #####
 */
function pyramid(input) {
    const calCol = input * 2 - 1;
    let midpoint = Math.floor(calCol / 2);
    for (let row = 0; row < input; row++) {
      let level = '';
      for (let col = 0; col < calCol; col++) {
        if (midpoint - row <= col && midpoint + row >= col) {
          level += '#';
        } else {
          level += ' ';
        }
      }
       console.log(level);
    }
}

// Alternative: build each row with string padStart/repeat instead of a
// character-by-character inner loop. Same O(n^2) total time, more concise.
function pyramidPad(input) {
    const width = input * 2 - 1;
    for (let row = 1; row <= input; row++) {
      const hashes = '#'.repeat(2 * row - 1);
      console.log(hashes.padStart(width - Math.floor((width - hashes.length) / 2)).padEnd(width));
    }
}

module.exports = pyramid;
module.exports.alternative = pyramidPad;
