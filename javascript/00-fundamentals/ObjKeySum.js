/**
 * Problem: Object Key Sum
 * Pattern: Fundamentals (object/array manipulation)
 * Time: O(n) | Space: O(k) where k = number of distinct keys
 *
 * Given an array of single-key objects, sum the values grouped by key.
 *
 * Input:  [{a: 2}, {a: 2}, {b: 1}, {b: 9}]
 * Output: { a: 4, b: 10 }
 */

function objKeySum(arr) {
    const output = {};
    arr.forEach(obj => {
        const key = Object.keys(obj)[0]; // assumes each object has only one key
        const value = obj[key];
        output[key] = (output[key] || 0) + value;
    });
    return output;
}

// Alternative: same idea expressed with reduce instead of forEach.
// Same O(n) time, more functional/one-line style.
function objKeySumReduce(arr) {
    return arr.reduce((output, obj) => {
        const key = Object.keys(obj)[0];
        output[key] = (output[key] || 0) + obj[key];
        return output;
    }, {});
}

console.log(objKeySum([{ a: 2 }, { a: 2 }, { b: 1 }, { b: 9 }])); // { a: 4, b: 10 }

module.exports = objKeySum;
module.exports.alternative = objKeySumReduce;
