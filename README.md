# DSA Daily Practice

Interviews want direct JS/Python, not a compiler step.

## Structure
Each pattern gets its own folder. JS solutions live next to their test file (Jest auto-discovers `*.test.js`).
```
python/<pattern>/<problem>.py
javascript/<pattern>/<problem>.js
javascript/<pattern>/<problem>.test.js   <- colocated Jest test
```

## Setup (one-time)
```bash
npm install                          # installs jest, for JS tests
pip install -r requirements.txt      # installs pytest, for Python tests
```
Python and JS need no other setup — just `python3` and `node` installed.

## How to run a single file
```bash
# Python
python3 python/02-two-pointers/two_sum_sorted.py

# JavaScript
node javascript/02-two-pointers/two_sum_sorted.js
```

## How to run ALL tests (proves nothing is broken/forgotten)
```bash
npm test                             # 173 JS tests across 33 files
python3 -m pytest                    # 107 Python tests across 34 files
```
Run these any time before/after a revision pass to catch regressions. `pytest.ini` at the repo
root points pytest at the `python/` folder, so `python3 -m pytest` works from anywhere in the repo.

## Patterns
| Folder | Pattern | Source |
|---|---|---|
| 00-fundamentals | Basics: recursion, closures, string/number manipulation | legacy repo |
| 01-arrays-hashing | Arrays, hashing, strings | both |
| 02-two-pointers | Two pointers | both |
| 03-sliding-window | Sliding window | new |
| 04-stack-queue | Stack, queue | both |
| 05-linked-list | Linked list | legacy repo |
| 06-binary-search | Binary search | (empty — add as you go) |
| 07-trees | Trees, BFS/DFS, BST | legacy repo |
| 08-graphs | Graphs, topological sort, union-find | (empty — add as you go) |
| 09-heap | Heaps / priority queues | (empty — add as you go) |
| 10-backtracking | Backtracking | (empty — add as you go) |
| 11-dp | Dynamic programming | legacy repo (fibonacci) |
| 12-greedy | Greedy | (empty — add as you go) |
| 13-intervals | Interval scheduling/merging | legacy repo |
| 14-matrix | Matrix construction/traversal | legacy repo |

## File template
Every solution file includes: problem statement, pattern, time/space complexity, a worked
input/output example, and a runnable entry point (`console.log` / `if __name__`) so it executes
standalone. Copy `_template.js` / `_template.py` when starting a new problem.

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