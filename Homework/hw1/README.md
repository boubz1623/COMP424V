# Homework 1 — Working Files

Source: `a1 - 2026.pdf`. Due Wednesday, September 30, 2026, at 9:00pm.

## Files

- **`q1_six_puzzle.py`** — Question 1(a). Implements breadth-first search (`bfs`), uniform-cost search (`ucs`), depth-first search (`dfs`), and iterative deepening (`ids`, using `dls`). `ucs` accepts an optional `cost_fn`; without one, moves have unit cost. The script prints each solution path.
- **`q3_search_optimization.py`** — Question 3. Implements hill climbing (`hc`) and local beam search (`beam`), along with the objective functions, neighbor generation, experiment runs, and summary tables. It uses 100 runs per setting and a fixed random seed for repeatable results. Beam search uses step size 0.1.
- **`424_ab.docx`** — Current written-answer draft, including puzzle paths, explanations for Question 2, and Question 3 results and observations. Prepare the written responses as one PDF for submission.
- **`a1 - 2026.pdf`** — Assignment instructions and questions.

## Running the code

From this folder, run:

```powershell
python q1_six_puzzle.py
python q3_search_optimization.py
```

Both scripts use only the Python standard library. The Q3 script prints tables; plotting is optional.

## Assignment reminders

- For Question 1, do not add explored states back to the search frontier. When priorities tie, prefer moving the lower-numbered piece; `get_successors` returns moves in that order.
- Submit written responses as one PDF and submit code separately, clearly labeled, as required by the assignment.
