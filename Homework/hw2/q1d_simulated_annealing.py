
import math
import random

START = [
    [2, 0, 4, 0],
    [0, 1, 0, 2],
    [1, 0, 0, 3],
    [0, 0, 0, 0],
]

FIXED = {(r,c) for r in range(4) for c in range(4) if START[r][c] != 0}

BOXES = [
    [(r, c) for r in range(br, br + 2) for c in range(bc, bc + 2)]
    for br in (0, 2) for bc in (0, 2)
]

RUNS = 100
MAX_STEPS = 10000

SETTINGS = {
    "A: T0=1.0, alpha=0.999": (1.0, 0.999),
    "B: T0=5.0, alpha=0.99": (5.0, 0.99),
    "C: T0=0.1, alpha=0.9": (0.1, 0.9),
}


def free_c(box):
    return [cell for cell in box if cell not in FIXED]

def rand_state():

    grid = [row[:] for row in START]
    for box in BOXES:
        present = {grid[r][c] for r,c in box if (r,c) in FIXED}
        missing = [d for d in range(1,5) if d not in present]
        random.shuffle(missing)

        for (r,c), d in zip(free_c(box), missing):
            grid[r][c] = d
    return grid


def violations(grid):
    total = 0
    for i in range(4):
        row = grid[i]
        col  = [grid[r][i] for r in range(4)]
        total += 4-len(set(row))
        total += 4 - len(set(col))
    return total

def random_neighbor(grid):

    box = random.choice(BOXES)
    (r1,c1), (r2,c2) = random.sample(free_c(box), 2)
    nxt =[row[:] for row in grid]
    nxt[r1][c1], nxt[r2][c2] = nxt[r2][c2], nxt[r1][c1]
    return nxt


def sa(t0, alpha, limit=MAX_STEPS, trace=0):
    grid = rand_state()
    cost = violations(grid)
    best, bst_cost = grid, cost
    temp = t0

    if trace:
        print("start, violations =", cost)
        show(grid)

    for step in range(1, limit+1):
        if bst_cost == 0:
            return best, True, step-1

        nxt = random_neighbor(grid)
        nxt_cost = violations(nxt)
        delta = nxt_cost-cost

        if delta < 0:

            grid, cost = nxt, nxt_cost
            if cost < bst_cost:
                best, bst_cost = grid, cost
            moved = "accepted"
        elif temp > 0 and random.random() < math.exp(-delta/temp):
            grid, cost = nxt, nxt_cost
            moved ="accepted"
        else:
            moved = "rejected"

        if step <= trace:
            print("step", step, "T =", round(temp, 4), "delta =", delta,
                  moved, "violations =", cost)
            show(grid)

        temp = temp*alpha

    return best, bst_cost == 0, limit


def show(grid):
    for r, row in enumerate(grid):
        line = " ".join(str(d) for d in row[:2]) + " | " + " ".join(str(d) for d in row[2:])
        print("  " + line)
        if r == 1:
            print("  ----+----")
    print()

def main():
    random.seed(67)

    print("First five steps, setting A")
  
    t0, alpha = SETTINGS["A: T0=1.0, alpha=0.999"]
    sa(t0, alpha, trace=5)

    print("Results over", RUNS, "runs, max", MAX_STEPS, "steps")


    for name, (t0,alpha) in SETTINGS.items():
        solved = 0
        steps = []
        for _ in range(RUNS):
            grid, ok, n =sa(t0, alpha)
            if ok:
                solved += 1
                steps.append(n)

        print(name)
        print("  solved:", solved, "/", RUNS)
        if steps:
            print("avg steps:", round(sum(steps)/len(steps), 1))
            print("max steps:",max(steps))

    print()
    print("Solution found:")
    show(grid)


if __name__ == "__main__":
    main()
