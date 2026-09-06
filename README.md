# DSA Daily Practice — Shubham Jain

Daily coding practice in **Python + JavaScript**, aligned with the 90-Day Job Switch Plan
(Senior Backend / Distributed Systems / Platform roles). Includes the full legacy `JS-DS-Interview`
repo, reorganized by pattern with tests filled in for every file. TypeScript was dropped —
interviews want direct JS/Python, not a compiler step.

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
Every solution file exposes a second, different way to solve the same problem — usually a
trade-off worth being able to explain in an interview (different time/space complexity, or a more
general version that works under looser assumptions). Convention:
- Bare function/class exports: `module.exports = mainFn; module.exports.alternative = altFn;`
- Object exports: the alternative is just another key in the exported object.

Examples: `two_sum_sorted.js` (two-pointer, needs sorted input) vs its hash-map alternative
(works unsorted, O(n) space); `max_sum_subarray.js` (sliding window, O(n)) vs brute force (O(n·k));
`paildrome.js` (reverse-and-compare) vs two-pointer (O(1) space instead of O(n));
`queue.js` (array-based) vs a linked-list-backed alternative with true O(1) add/remove.

## Bugs found and fixed while merging the legacy repo
A full audit of every JS file — not just `00-fundamentals` — surfaced 11 genuine issues. This is
exactly the value of daily practice + tests: a bug or wrong comment sitting untested for years gets
caught the moment you write a real test against it.
- **`characterCount.js` → `countAllChar`**: counted from 1 instead of 0 (`count[item] || 1`), inflating
  every character count by one. Fixed to `count[item] || 0`.
- **`rockPaperScissors.js`**: two functions were both named `playRPS` — the second silently overwrote
  the first (same-name redeclaration), so the 2-player version was dead code. Renamed to
  `playRPSTwoPlayer` and `playRPSVsComputer`, both now exported and tested.
- **`mergeIntervals.js`**: typo `intervals.lenght` (should be `.length`) meant the empty-array guard
  never fired. Fixed.
- **`curning.js`**: filename typo (should be "currying") and no problem statement at all. Renamed to
  `currying.js`, added proper docstrings, and exported the `get()` fluent-API function that was
  written but never wired into `module.exports`.
- **`curning.js`'s own inline comments were wrong**: claimed the chainable-API example outputs `20`
  (actual math gives `15`), and implied `closure()` demonstrates the classic `var`-in-a-loop bug
  (would print `3, 3, 3`) — it actually prints `0, 1, 2` correctly, because `i` is passed as an
  argument to `print()`, creating a fresh binding per call. Fixed both the docstring and test.
- **`fizzbuzz.js`**: the array-returning function (renamed `fizbuzz` → `fizzBuzzArray`) had typos in
  its own output strings — `'fiz'` and `'fizbuzz'` instead of `'fizz'` and `'fizzbuzz'` — and had zero
  test coverage. Fixed and added tests.
- **`factorial.js` → `factorialRecur`**: claimed to be recursive but called `factorial(n - 1)` (the
  iterative version) instead of calling itself — never actually recursed past one level. Fixed to
  call `factorialRecur(n - 1)`.
- **`steps.js` → `stepsLTR`**: off-by-one bug meant row 0 printed zero hashes instead of one —
  `stepsLTR(3)` gave `['', '#', '##']` instead of `['#', '##', '###']`. Had zero test coverage (only
  `steps` was tested, not the other 3 functions in the file). Fixed the loop and added tests for all
  4 functions.
- **`queue.js`'s own doc comment was wrong**: described a queue as "LIFO" — that's a stack. A queue
  is FIFO. Fixed the docstring.
- **`makeMatrix.js`'s own example comment was wrong**: claimed `matrix(2)` produces
  `[[undefined, undefined], [undefined, undefined]]` — verified by running it that this is false; it
  correctly produces `[[1, 2], [4, 3]]`. Added a regression test for this exact case.
- **`LinkList.js`**: the `append` method existed and worked correctly but had **zero test coverage**
  (not referenced anywhere in the original test file). Added tests.

- **`level_width.py`'s Python port of the sentinel alternative had a JS-vs-Python truthiness bug**:
  the JS original checks `node.children` truthiness to decide whether to count a node — and in JS,
  an empty array is still truthy. Porting that check directly to Python as `if node.children:`
  silently skipped leaf nodes (Python's empty list is falsy), undercounting levels with leaves.
  Fixed by checking `hasattr(node, 'children')` instead of the list's truthiness — a good example of
  a bug that only appears when porting between languages with different truthiness rules.

Every JS file across all 15 pattern folders now has a complete docstring: problem statement, pattern,
time/space complexity, and a worked input/output example — many had none, or only a partial comment,
before this audit. **All 32 legacy problems (plus the 2 new ones) are now ported to Python as well,
with full pytest coverage** — 107 Python tests, 34 files, all passing, matching the JS structure
1-to-1 by pattern folder.

## Daily Log
| Date | Problem | Pattern | Python | JS | Notes |
|------|---------|---------|--------|----|----|
| 2026-09-06 | Two Sum II (sorted) | Two Pointers | ✅ | ✅ | + hash-map alternative |
| 2026-09-06 | Max Sum Subarray (size K) | Sliding Window | ✅ | ✅ | + brute-force alternative |
| 2026-09-06 | Migrated 32 legacy exercises (JS-DS-Interview) | Various | ✅ | ✅ | 173 JS tests + 107 Python tests, 12 issues fixed, every file has a full docstring + alternative method, full Python port with 1 additional truthiness bug caught during porting |

## Progress toward 90-Day Plan targets
- Day 30 target: 30–40 problems
- Day 60 target: 70–80 problems
- Day 90 target: 100–120 problems
- **Current: 34 problems in both JS and Python (32 legacy + 2 new), full parity between languages**
