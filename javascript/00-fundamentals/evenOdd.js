/**
 * Problem: Even or Odd
 * Pattern: Fundamentals (modulo, array generation)
 * Time: O(1) for checkEvenOdd, O(n) for printEvenOdd | Space: O(1) / O(n)
 *
 * checkEvenOdd: classify a single positive number as even or odd.
 * printEvenOdd: label every number from 1 to n as even or odd.
 *
 * Input:  checkEvenOdd(4)
 * Output: 'Even number'
 *
 * Input:  printEvenOdd(2)
 * Output: ['1: Odd Number', '2: Even Number']
 */
function checkEvenOdd(input) {
    if(input <= 0) return 'Not valid number';
    return (input % 2 == 0) ? 'Even number' :  'Odd number';
}

function printEvenOdd(input) {
   if(input <= 0) return 'Not valid number';
   return Array.from({length: input}, (_, index) => { 

     return  `${index+1}: ${((index+1)%2 == 0) ? 'Even Number' : 'Odd Number'}`
   })
  }

module.exports = {
  printEvenOdd,
  checkEvenOdd
}