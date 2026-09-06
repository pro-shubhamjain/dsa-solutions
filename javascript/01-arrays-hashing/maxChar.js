// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
//
// Approach 1: hash map of counts, then linear scan for the max (below)
// Approach 2 (alternative): sort characters, then count runs of equal
// adjacent chars in one pass -- O(n log n) instead of O(n), but avoids
// building an explicit frequency map. Useful to mention as a trade-off
// in interviews even though approach 1 is strictly better here.

function maxChar(input) {
    const charCount = {};
    input.replace(/[^\w]/g, '').split('').forEach(char => {
        charCount[char] = (charCount[char] || 0) + 1;
    });
  
    let maxChar = '';
    let maxCount = 0;
  
    for (const char in charCount) {
        if (charCount[char] > maxCount) {
            maxCount = charCount[char];
            maxChar = char;
        }
    }

    //`{ ${maxChar} : ${maxCount} }`
  
    return maxChar; 
}

// Alternative: sort + count runs. Time: O(n log n) | Space: O(n)
function maxCharSorted(input) {
    const chars = input.replace(/[^\w]/g, '').split('').sort();
    let maxChar = '';
    let maxCount = 0;
    let currentChar = '';
    let currentCount = 0;

    for (const char of chars) {
        if (char === currentChar) {
            currentCount++;
        } else {
            currentChar = char;
            currentCount = 1;
        }
        if (currentCount > maxCount) {
            maxCount = currentCount;
            maxChar = currentChar;
        }
    }
    return maxChar;
}

module.exports = maxChar;
module.exports.alternative = maxCharSorted;
  
