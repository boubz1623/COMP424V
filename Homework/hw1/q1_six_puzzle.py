

from collections import deque
import itertools

ROWS, COLS = 2, 3
BLANK = 0

INITIAL_STATE = (1, 4, 2, 5, 3, 0)
GOAL_STATE = (0, 1, 2, 5, 4, 3)


def blank_index(state):
    return state.index(BLANK)


def index_to_rc(index):
    return divmod(index, COLS)


def rc_to_index(row, col):
    return row * COLS + col


def get_successors(state):
 
    b_idx = blank_index(state)
    b_row, b_col = index_to_rc(b_idx)

    successors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dr, dc in moves:
        nr, nc = b_row + dr, b_col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            n_idx = rc_to_index(nr, nc)
            piece_moved = state[n_idx]
            new_state = list(state)
            new_state[b_idx], new_state[n_idx] = new_state[n_idx], new_state[b_idx]
            successors.append((piece_moved, tuple(new_state)))

    successors.sort(key=lambda pair: pair[0])
    return successors


def state_to_str(state):
    rows = []
    for r in range(ROWS):
        row_tiles = state[r * COLS:(r + 1) * COLS]
        rows.append(" ".join("_" if t == BLANK else str(t) for t in row_tiles))
    return "\n".join(rows)


def reconstruct_path(came_from, state):

    path = []
    current = state
    while current is not None:
        prev, piece_moved = came_from[current]
        path.append((piece_moved, current))
        current = prev
    path.reverse()
    return path


def print_solution(path):
    """Print a solution path returned by reconstruct_path()."""
    for step_num, (piece_moved, state) in enumerate(path):
        if piece_moved is None:
            print(f"Step {step_num} (initial state):")
        else:
            print(f"Step {step_num} (moved piece {piece_moved}):")
        print(state_to_str(state))
        print()


def breadth_first_search(start=INITIAL_STATE, goal=GOAL_STATE):
    """
    Solve the puzzle with BFS.

    Must not re-add explored states to the queue. When multiple successors
    are otherwise equivalent in priority, prefer the one that moves the
    lower-numbered piece (see get_successors, which already returns
    successors sorted by piece number).

    Returns a list of (piece_moved, state) tuples describing the solution
    path from start to goal (see reconstruct_path), or None if no
    solution is found.
    """
    # TODO: implement BFS using a FIFO queue (collections.deque) and a
    # `visited` set / `came_from` dict as described above.
    raise NotImplementedError


def uniform_cost_search(start=INITIAL_STATE, goal=GOAL_STATE, cost_fn=None):
    """
    Solve the puzzle with Uniform Cost Search.

    cost_fn(piece_moved) -> int/float gives the cost of moving a given
    piece. Defaults to unit cost (every move costs 1), matching part (a).
    For part (b)/(c) you can pass cost_fn=lambda piece: piece.

    Returns a list of (piece_moved, state) tuples describing the solution
    path from start to goal, or None if no solution is found.
    """
    if cost_fn is None:
        cost_fn = lambda piece: 1

    # TODO: implement UCS using a priority queue (heapq) keyed on path
    # cost so far, breaking ties by preferring the lower-numbered piece
    # moved. Don't re-expand states already finalized (popped) before.
    raise NotImplementedError


def depth_first_search(start=INITIAL_STATE, goal=GOAL_STATE):
    """
    Solve the puzzle with DFS (graph-search version: do not re-expand
    already-visited states).

    Returns a list of (piece_moved, state) tuples describing the solution
    path from start to goal, or None if no solution is found.
    """
    # TODO: implement DFS using an explicit stack and a `visited` set.
    raise NotImplementedError


def depth_limited_search(start, goal, limit):
    """
    Helper for iterative deepening: DFS cut off at depth `limit`.

    Returns a list of (piece_moved, state) tuples if a solution is found
    within the depth limit, or None otherwise.
    """
    # TODO: implement depth-limited DFS.
    raise NotImplementedError


def iterative_deepening_search(start=INITIAL_STATE, goal=GOAL_STATE, max_limit=50):
    """
    Solve the puzzle with Iterative Deepening Search, calling
    depth_limited_search with increasing depth limits.

    Returns a list of (piece_moved, state) tuples describing the solution
    path from start to goal, or None if no solution is found within
    max_limit.
    """
    # TODO: call depth_limited_search(start, goal, limit) for
    # limit = 0, 1, 2, ... until a solution is found or max_limit reached.
    raise NotImplementedError


if __name__ == "__main__":
    print("=== Breadth First Search ===")
    solution = breadth_first_search()
    if solution:
        print_solution(solution)

    print("=== Uniform Cost Search (unit cost) ===")
    solution = uniform_cost_search()
    if solution:
        print_solution(solution)

    print("=== Depth First Search ===")
    solution = depth_first_search()
    if solution:
        print_solution(solution)

    print("=== Iterative Deepening Search ===")
    solution = iterative_deepening_search()
    if solution:
        print_solution(solution)
