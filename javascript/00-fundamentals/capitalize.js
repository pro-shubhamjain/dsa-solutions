/**
 * Problem: Capitalize
 * Pattern: Fundamentals (string manipulation)
 * Time: O(n) | Space: O(n)
 *
 * Capitalize the first letter of every word in a sentence.
 *
 * Input:  "hi there, how is it going?"
 * Output: "Hi There, How Is It Going?"
 */
function capitalize(input) {
    return input
      .split(' ')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
 }


 // Alternative: explicit for-loop instead of split/map/join (this was the
 // original commented-out beginner version in this file -- wiring it up
 // instead of leaving it dead code). Same O(n) time, less concise.
 function capitalizeLoop(input) {
    if (input === '') return input;
    let words = input.split(' ');
    for (let i = 0; i < words.length; i++) {
      words[i] = words[i][0].toUpperCase() + words[i].substring(1);
    }
    return words.join(' ');
 }

 console.log(capitalize('hi there, how is it going?')); // "Hi There, How Is It Going?"

 module.exports = capitalize;
 module.exports.alternative = capitalizeLoop;