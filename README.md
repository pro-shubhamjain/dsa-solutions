# DSA Daily Practice

Interviews want direct JS, not a compiler step.

## Structure
Each pattern gets its own folder. Solutions live next to their test file (Jest auto-discovers `*.test.js`).
```
javascript/<pattern>/<problem>.js
javascript/<pattern>/<problem>.test.js   <- colocated Jest test
```

## Setup (one-time)
```bash
npm install                          # installs jest, for JS tests
```
Just `node` installed, no other setup needed.

## How to run a single file
```bash
node javascript/02-two-pointers/two_sum_sorted.js
```

## How to run ALL tests (proves nothing is broken/forgotten)
```bash
npm test                             # runs all JS tests
```
Run this any time before/after a revision pass to catch regressions.

## Patterns
| Folder | Pattern |
|---|---|
| 00-fundamentals | Basics: recursion, closures, string/number manipulation |
| 01-arrays-hashing | Arrays, hashing, strings |
| 02-two-pointers | Two pointers |
| 03-sliding-window | Sliding window |
| 04-stack-queue | Stack, queue |
| 05-linked-list | Linked list |
| 06-binary-search | Binary search (empty — add as you go) |
| 07-trees | Trees, BFS/DFS, BST |
| 08-graphs | Graphs, topological sort, union-find (empty — add as you go) |
| 09-heap | Heaps / priority queues (empty — add as you go) |
| 10-backtracking | Backtracking (empty — add as you go) |
| 11-dp | Dynamic programming |
| 12-greedy | Greedy (empty — add as you go) |
| 13-intervals | Interval scheduling/merging |
| 14-matrix | Matrix construction/traversal |

## File template
Every solution file includes: problem statement, pattern, time/space complexity, a worked
input/output example, and a runnable entry point (`console.log`) so it executes standalone.
Copy `_template.js` when starting a new problem.

## Every problem now has an alternative approach
Every solution file exposes a second, different way to solve the same problem - usually a
trade-off worth being able to explain in an interview (different time/space complexity, or a more
general version that works under looser assumptions). Convention:
- Bare function/class exports: `module.exports = mainFn; module.exports.alternative = altFn;`
- Object exports: the alternative is just another key in the exported object.

Examples: `two_sum_sorted.js` (two-pointer, needs sorted input) vs its hash-map alternative
(works unsorted, O(n) space); `max_sum_subarray.js` (sliding window, O(n)) vs brute force (O(n·k));
`paildrome.js` (reverse-and-compare) vs two-pointer (O(1) space instead of O(n));
`queue.js` (array-based) vs a linked-list-backed alternative with true O(1) add/remove.
