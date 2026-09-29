# Homework 1 — Written Answers

(Scaffold — fill in, then convert to PDF for submission. Code goes in
separate files: `q1_six_puzzle.py`, `q3_search_optimization.py`.)

## Question 1: Six-Puzzle

### a) Solution paths

i. **Breadth first search**
- Solution path:

ii. **Uniform cost search**
- Solution path:

iii. **Depth first search**
- Solution path:

iv. **Iterative deepening**
- Solution path:

### b) Is Manhattan distance still admissible under the new cost scheme?

(Cost of moving piece k is k, instead of unit cost. Justify whether
Manhattan distance — sum over tiles of |row difference| + |col
difference| between current and goal position — remains a lower bound
on true remaining cost.)

### c) A heuristic dominating (b)'s heuristic

(Design h'(n) >= h(n) for all n, still admissible, under the same
cost-per-piece scheme. Justify admissibility and domination.)

## Question 2: Search algorithms

### a) State space where IDS performs much worse than DFS

### b) BFS is a special case of UCS — prove or give counterexample

### c) DFS is a special case of best-first tree search — prove or give counterexample

### d) Best-first search is optimal with a perfect heuristic — prove or give counterexample

### e) With a unique optimal solution, A* with a perfect heuristic never expands nodes off the optimal path

### f) A* is optimal with negative edge weights allowed — prove or give counterexample

## Question 3: Search for Optimization

### a) Hill climbing (100 random starts x step sizes [0.01, 0.05, 0.1, 0.2])

- Results table / plot for f1:
- Results table / plot for f2:
- Patterns observed:

### b) Local beam search (100 runs x beam widths [2, 4, 8, 16])

- Results table / plot for f1:
- Results table / plot for f2:
- Comparison to hill climbing:
