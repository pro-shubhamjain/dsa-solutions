
/**
 * Problem: Character Count / Run-Length Encoding
 * Pattern: Arrays & Hashing (string traversal)
 * Time: O(n) | Space: O(n)
 *
 * countCharSerlize: run-length-encode a string -- each run of repeated
 * characters becomes "<char><count>".
 * countAllChar: count total occurrences of every character in a string
 * (not run-based -- occurrences anywhere, not just consecutive).
 *
 * Input:  countCharSerlize("abbbccddddaab")
 * Output: "a1b3c2d4a2b1"
 *
 * Input:  countAllChar("aabbbc")
 * Output: { a: 2, b: 3, c: 1 }
 */
function countCharSerlize(string) {
    let str = string;
    let count = 1;
    let result = '';
     for(let i = 0; i <  str.length ;i++) {
         if(str[i] == str[i+1]) {
             count ++
         } else {
            result += str[i] + count;
            count = 1;
         }
     }
    return result;
}

function countAllChar(string) {
   const arrString = string.replace(/[^a-z0-9]/gi,'').split('');
   return arrString.reduce((count, item) =>{
      count[item] = (count[item] || 0) + 1;
       return count;  
   } ,{}); 
}

module.exports = { countCharSerlize, countAllChar};