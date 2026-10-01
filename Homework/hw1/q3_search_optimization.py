import math
import random
import statistics

X_LO, X_HI = 0.0, 10.0
Y_LO, Y_HI = 0.0, 10.0

STEPS = [0.01, 0.05, 0.1, 0.2]
WIDTHS = [2, 4, 8, 16]
RUNS = 100


def f1(x, y):
    return math.sin(2 * x) + math.cos(y / 2)


def f2(x, y):
    return abs(x - 2) +abs(0.5 * y + 1) - 4


def rand_pt():
    return random.uniform(X_LO, X_HI),  random.uniform(Y_LO, Y_HI)

 
def neighbors(x, y, step):
    next_pts = []
    for dx in (-step, 0.0,step):
        for dy in (-step, 0.0, step):
            if dx == 0.0 and dy == 0.0:
                continue
            nx, ny = x+ dx,  y + dy
            if X_LO <= nx<= X_HI and Y_LO <= ny <= Y_HI:
                next_pts.append( (nx, ny))
    return next_pts

 
def hc(fn, step, start=None, limit=10000):
    if start is  None:
        start =rand_pt()
    x, y = start
    val = fn(x, y)
    count = 0

    while count <limit:
        bx, by = x, y
        best = val

        for nx, ny in  neighbors(x, y, step):
            cand = fn(nx, ny)
            if cand > best:
                bx,by = nx, ny
                best = cand

        if best ==val:
            break

        x, y, val = bx, by, best
        count += 1

    return x, y, val,  count


def beam(fn, step, width,limit=10000):
    front = [rand_pt() for  _ in range(width)]
    best_pt = max(front, key=lambda pt: fn(*pt))
    best_val =  fn( *best_pt)
    count = 0

    while count < limit:
        pool = {pt: fn(*pt) for  pt in front}
        for x, y in front:
            for pt in neighbors(x,  y, step):
                if pt not in pool:
                    pool[pt] = fn(*pt)

        top = sorted(pool.items(),  key=lambda item: item[1], reverse=True)[:width]
        count += 1

        if top[0][1] <= best_val:
            break

        front = [pt for pt, _ in  top]
        best_pt, best_val = top[0]

    return best_pt[0],  best_pt[1], best_val, count


def run_hc(fn, step,  runs=RUNS):
    counts = []
    vals = []
    for _ in range(runs):
        _, _, val, count = hc(fn, step)
        counts.append(count)
        vals.append(val)

    return {
        "avg_steps": statistics.mean(counts),
        "sd_steps": statistics.pstdev(counts),
        "avg_val": statistics.mean(vals),
        "sd_val": statistics.pstdev(vals),
    }


def run_beam(fn, step, width, runs=RUNS):
    counts = []
    vals = []
    for _ in range(runs):
        _, _, val, count  = beam(fn, step, width)
        counts.append(count)
        vals.append(val)

    return {
        "avg_steps": statistics.mean(counts),
        "sd_steps": statistics.pstdev(counts),
        "avg_val":  statistics.mean(vals),
        "sd_val": statistics.pstdev(vals),
    }


def print_table(title, rows, headers):
    print(f"\n{title}")
    widths = []
    for idx, header in enumerate(headers):
        cells = [
            f"{row[idx]:.4f}" if isinstance(row[idx], float) else str(row[idx])
            for row in rows
        ]
        widths.append(max(len(str(header)), *(len(cell) for cell in cells)))

    hdr = " | ".join(header.ljust(width) for header, width in zip(headers, widths))
    print(hdr)
    print("-" * len(hdr))
    for row in rows:
        cells = [
            f"{val:.4f}".ljust(width)
            if isinstance(val, float)
            else str(val).ljust(width)
            for val, width in zip(row, widths)
        ]
        print(" | ".join(cells))


if __name__ == "__main__":
    random.seed(424)
    funcs = {"f1": f1, "f2": f2}

    for name, fn in funcs.items():
        rows = []
        for step in STEPS:
            res = run_hc(fn, step)
            rows.append(
                (
                    step,
                    res["avg_steps"],
                    res["sd_steps"],
                    res["avg_val"],
                    res["sd_val"],
                )
            )
        print_table(
            f"Hill Climbing on {name}",
            rows,
            ["step_size", "mean_steps", "std_steps", "mean_value", "std_value"],
        )

    for name, fn in funcs.items():
        rows = []
        for width in WIDTHS:
            res = run_beam(fn, step=0.1, width=width)
            rows.append(
                (
                    width,
                    res["avg_steps"], 
                    res["sd_steps"],
                    res["avg_val"],
                    res["sd_val"],
                )
            )
        print_table(
            f"Local Beam Search on {name} (step size 0.1)",
            rows,
            ["beam_width", "mean_steps", "std_steps", "mean_value", "std_value"],
        )
