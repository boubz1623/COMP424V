# Homework 1 — Working Files

Source: `a1 - 2026.pdf`. Due Wed Sept 30, 9:00pm.

## Files

- **`q1_six_puzzle.py`** — Question 1 (Six-Puzzle), part (a).
  Board representation, successor generation, path reconstruction, and
  printing are implemented. The four search algorithms
  (`breadth_first_search`, `uniform_cost_search`, `depth_first_search`,
  `iterative_deepening_search` / `depth_limited_search`) are `TODO` stubs
  for you to fill in.
  - Parts (b) and (c) (admissibility of Manhattan distance under the new
    cost scheme, and designing a dominating heuristic) are written-answer
    questions — no code required, but you could extend this file with an
    `a_star_search(start, goal, heuristic, cost_fn)` if you want to
    empirically sanity-check a heuristic.

- **`q3_search_optimization.py`** — Question 3 (Search for Optimization).
  `f1`, `f2`, neighbor generation, random sampling, and the
  experiment/statistics/reporting scaffolding are implemented.
  `hill_climbing` and `local_beam_search` are `TODO` stubs for you to
  fill in. Running the file prints result tables for part (a) (step
  sizes) and part (b) (beam widths); feel free to swap the tables for
  the plots the assignment suggests.

- **`answers.md`** — scaffold for the written answers (Q1 a/b/c solution
  paths and heuristic discussion, Q2 a–f, Q3 discussion of patterns).
  Fill in and convert to PDF (or write by hand) for submission — the
  assignment requires a single PDF of written responses, with code
  submitted separately.

## Running

```
python "q1_six_puzzle.py"
python "q3_search_optimization.py"
```

Both are pure-Python (only `math`, `random`, `statistics`, `collections`
from the standard library) — no extra installs needed. If you add
plotting for Q3, `matplotlib` is the natural choice (`pip install
matplotlib`).

## Reminders from the assignment

- Q1: previously-explored states must not be re-added to the search
  queue; break ties by preferring to move the lower-numbered piece
  (`get_successors` already returns successors sorted by piece number
  ascending, which makes this easy to respect in each algorithm).
- Submit written answers as a single PDF, and code for Q1 and Q3 as
  separate files, clearly labeled.
