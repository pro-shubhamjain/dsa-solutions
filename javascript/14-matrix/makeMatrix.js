// --- Directions
// Write a function that accepts an integer N
// and returns a NxN spiral matrix.
//
// Problem: Spiral Matrix
// Pattern: Matrix traversal (boundary shrinking)
// Time: O(n^2) | Space: O(n^2)
//
// BUG FOUND in the original comment: it claimed matrix(2) produces
// [[undefined, undefined], [undefined, undefined]]. Actually verified by
// running it -- matrix(2) correctly produces [[1, 2], [4, 3]].
// --- Examples
//   matrix(2)
//     [[1, 2],
//     [4, 3]]
//matrix(3);
//     [[1, 2, 3],
//     [8, 9, 4],
//     [7, 6, 5]]


function matrix(n) {
  const results = [];

  for (let i = 0; i < n; i++) {
    results.push([]);
  }

  let counter = 1;
  let startColumn = 0;
  let endColumn = n - 1;
  let startRow = 0;
  let endRow = n - 1;
  while (startColumn <= endColumn && startRow <= endRow) {
    // Top row
    for (let i = startColumn; i <= endColumn; i++) {
      results[startRow][i] = counter;
      counter++;
    }
    startRow++;

    // Right column
    for (let i = startRow; i <= endRow; i++) {
      results[i][endColumn] = counter;
      counter++;
    }
    endColumn--;

    // Bottom row
    for (let i = endColumn; i >= startColumn; i--) {
      results[endRow][i] = counter;
      counter++;
    }
    endRow--;

    // start column
    for (let i = endRow; i >= startRow; i--) {
      results[i][startColumn] = counter;
      counter++;
    }
    startColumn++;
  }

  console.log(results);
  return results;
}

// Alternative: direction-vector simulation (walk right/down/left/up, turning
// when the next cell would leave bounds or has already been filled) instead
// of tracking four shrinking boundaries. Same O(n^2) time -- this pattern
// generalizes better to non-square spiral problems (e.g. spiral over a
// rectangular m x n grid), so it's worth knowing both.
function matrixDirectionVector(n) {
  const results = Array.from({ length: n }, () => new Array(n).fill(null));
  const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]; // right, down, left, up
  let dirIndex = 0;
  let row = 0, col = 0;

  for (let counter = 1; counter <= n * n; counter++) {
    results[row][col] = counter;
    const [dr, dc] = directions[dirIndex];
    const nextRow = row + dr, nextCol = col + dc;

    const outOfBounds = nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= n;
    const alreadyFilled = !outOfBounds && results[nextRow][nextCol] !== null;

    if (outOfBounds || alreadyFilled) {
      dirIndex = (dirIndex + 1) % 4;
    }
    row += directions[dirIndex][0];
    col += directions[dirIndex][1];
  }

  return results;
}

module.exports = matrix;
module.exports.alternative = matrixDirectionVector;
