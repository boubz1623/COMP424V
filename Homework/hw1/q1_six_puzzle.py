

from collections import deque
import heapq

ROWS, COLS = 2, 3
BLANK = 0

I_STATE = (1, 4, 2, 5, 3, 0)
G_STATE = (0, 1, 2, 5, 4, 3)


def blank_idx(state):
    for idx, tile in enumerate(state):
        if tile ==BLANK:
            return idx


def idx_to_rc(idx):
    return divmod(idx, COLS)


def rc_to_idx(row, col):
    return row *COLS + col


def get_successors(state):
 
    b_idx = blank_idx( state)
    b_row, b_col = idx_to_rc(b_idx )

    next_sts = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = b_row + dr, b_col + dc
        if 0 <= nr <ROWS and 0  <= nc < COLS:
            n_idx  = rc_to_idx(nr, nc)
            moved = state[n_idx]
            new_st =list(state)
            new_st[b_idx], new_st[n_idx] = new_st[n_idx], new_st[b_idx]
            next_sts.append((moved, tuple(new_st)))

    next_sts.sort(key=lambda pair: pair[0])
    return next_sts


def state_to_str(state):
    rows = []
    for r in range(ROWS):
        row_tiles = state[r * COLS:(r + 1) * COLS]
        rows.append(" ".join( "_" if t == BLANK else str(t) for t in row_tiles))
    return "\n".join(rows)


def reconstruct_path(parent, state):

    path = []
    current = state
    while current is not None:
        prev, moved  = parent[current]
        path.append( (moved, current))
        current = prev
    path.reverse()
    return path


def print_solution(path):
    for step_num, (moved, state) in enumerate(path):
        if moved is None:
            print( f"Step {step_num} (initial state):")
        else:
            print(f"Step {step_num} (moved piece {moved}):")
        print(state_to_str(state ))
        print()


def bfs(start=I_STATE, goal=G_STATE):
    front = deque([start])
    disc = {start}
    parent = {start: (None, None)}

    while front:
        state = front.popleft()
        if state == goal:
            return reconstruct_path(parent, state)

        for moved, next_st in get_successors(state):
            if next_st not in disc:
                disc.add(next_st)
                parent[next_st] =(state, moved)
                front.append(next_st)

    return None


def ucs(start=I_STATE, goal=G_STATE,cost_fn=None):
    if cost_fn is None:
        cost_fn = lambda piece: 1

    front = [(0, 0, start)]
    costs = {start: 0}
    done = set()
    parent ={start: (None, None)}

    while front:
        path_cost, _, state = heapq.heappop(front)
        if state in done:
            continue
        done.add(state)

        if state == goal:
            return  reconstruct_path(parent, state)

        for moved, next_st in get_successors(state):
            if next_st in done:
                continue
            new_cost = path_cost + cost_fn(moved)
            if new_cost <costs.get(next_st, float("inf")):
                costs[next_st] = new_cost
                parent[next_st] = (state, moved)
                heapq.heappush(front, (new_cost, moved, next_st))

    return None


def dfs(start=I_STATE, goal=G_STATE):
    front = [start]
    visited = {start}
    parent = {start: (None, None)}

    while front:
        state = front.pop()
        if state == goal:
            return reconstruct_path(parent, state)

        for moved, next_st in reversed(get_successors(state)):
            if next_st not in visited:
                visited.add(next_st)
                parent[next_st] = (state, moved)
                front.append(next_st)

    return None


def dls(start, goal, limit):
    front = [(start, 0)]
    depths = {start: 0}
    expanded = {}
    parent = {start: (None, None)}

    while front:
        state, depth = front.pop() 
        if depth != depths[state]:
            continue
        if expanded.get(state, limit + 1) <= depth:
            continue
        expanded[state] = depth

        if state == goal:
            return reconstruct_path(parent, state)
        if depth == limit:
            continue

        for moved, next_st in reversed(get_successors(state)):
            new_depth = depth + 1
            if new_depth < depths.get(next_st, limit + 1):
                depths[next_st] = new_depth
                parent[next_st] = (state, moved)
                front.append((next_st, new_depth))

    return None


def ids(start=I_STATE, goal=G_STATE, max_limit=50):
    for limit in range(max_limit + 1):
        path =  dls(start, goal, limit)
        if path is not None:
            return path
    return None


if __name__ == "__main__":
    print("=== BFS ===")
    solution = bfs()
    if solution:
        print_solution(solution)

    print("=== UCS ===")
    solution = ucs()
    if solution:
        print_solution(solution)

    print("=== DFS ===")
    solution = dfs()
    if solution:
        print_solution(solution)

    print("=== IDS ===")
    solution = ids()
    if solution:
        print_solution(solution)
