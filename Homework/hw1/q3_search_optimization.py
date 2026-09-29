"""
COMP-424 Homework 1, Question 3: Search for Optimization

Maximize:
    f1(x, y) = sin(2x) + cos(y / 2)
    f2(x, y) = |x - 2| + |0.5y + 1| - 4

over 0 <= x, y <= 10, using:
    (a) hill climbing, from 100 random starting points, for step sizes in
        [0.01, 0.05, 0.1, 0.2]
    (b) local beam search, 100 runs, for beam widths in [2, 4, 8, 16]

For each (function, algorithm, setting) combination, report the mean and
standard deviation of:
    - the number of steps to convergence
    - the final value f1*/f2* reached

TODO for you: implement hill_climbing() and local_beam_search(). The
objective functions, neighbor generation, random sampling, and the
experiment/reporting scaffolding are provided.
"""

import math
import random
import statistics

X_MIN, X_MAX = 0.0, 10.0
Y_MIN, Y_MAX = 0.0, 10.0

STEP_SIZES = [0.01, 0.05, 0.1, 0.2]
BEAM_WIDTHS = [2, 4, 8, 16]
NUM_RUNS = 100


def f1(x, y):
    return math.sin(2 * x) + math.cos(y / 2)


def f2(x, y):
    return abs(x - 2) + abs(0.5 * y + 1) - 4


def random_point():
    """Sample a uniformly random (x, y) in [0, 10] x [0, 10]."""
    return random.uniform(X_MIN, X_MAX), random.uniform(Y_MIN, Y_MAX)


def clip(value, lo, hi):
    """Clamp value into [lo, hi]."""
    return max(lo, min(hi, value))


def get_neighbors(x, y, step):
    """
    Return the (up to 8) neighbors of (x, y) for the given step size:
    x and/or y each individually unchanged / +step / -step, excluding
    (x, y) itself, and excluding points outside [0, 10] x [0, 10].
    """
    neighbors = []
    for dx in (-step, 0.0, step):
        for dy in (-step, 0.0, step):
            if dx == 0.0 and dy == 0.0:
                continue
            nx, ny = x + dx, y + dy
            if X_MIN <= nx <= X_MAX and Y_MIN <= ny <= Y_MAX:
                neighbors.append((nx, ny))
    return neighbors


def hill_climbing(func, step, start=None, max_steps=10000):
    """
    Steepest-ascent hill climbing on `func`, starting at `start` (or a
    random point if None), using neighbors generated with the given
    step size. Stops when no neighbor improves on the current point
    (a local optimum), or after max_steps.

    Returns (final_x, final_y, final_value, num_steps).
    """
    if start is None:
        start = random_point()
    x, y = start

    # TODO: implement steepest-ascent hill climbing:
    #   1. Evaluate func at all neighbors of (x, y).
    #   2. Move to the best neighbor if it improves on func(x, y).
    #   3. Otherwise stop (local optimum reached).
    #   4. Track the number of steps (moves) taken.
    raise NotImplementedError


def local_beam_search(func, step, beam_width, max_steps=10000):
    """
    Local beam search on `func` with `beam_width` parallel states,
    each initialized to a random point, using neighbors generated with
    the given step size.

    Returns (final_x, final_y, final_value, num_steps), where
    (final_x, final_y, final_value) is the best state found across the
    beam when the search terminates (e.g., no candidate in the combined
    neighbor pool improves on the current best beam), and num_steps is
    the number of iterations performed.
    """
    beam = [random_point() for _ in range(beam_width)]

    # TODO: implement local beam search:
    #   1. At each iteration, generate all neighbors of all states
    #      currently in the beam.
    #   2. Keep the top `beam_width` states (by func value) among the
    #      combined pool of current beam + neighbors.
    #   3. Stop when the new beam doesn't improve over the old one
    #      (e.g., best value unchanged), or after max_steps iterations.
    #   4. Track the number of iterations taken.
    raise NotImplementedError


def run_hill_climbing_experiment(func, step, num_runs=NUM_RUNS):
    """
    Run hill_climbing `num_runs` times (each from a fresh random start)
    and return summary statistics.

    Returns a dict with keys: mean_steps, std_steps, mean_value, std_value.
    """
    steps_list = []
    values_list = []
    for _ in range(num_runs):
        _, _, value, steps = hill_climbing(func, step)
        steps_list.append(steps)
        values_list.append(value)

    return {
        "mean_steps": statistics.mean(steps_list),
        "std_steps": statistics.pstdev(steps_list),
        "mean_value": statistics.mean(values_list),
        "std_value": statistics.pstdev(values_list),
    }


def run_beam_search_experiment(func, step, beam_width, num_runs=NUM_RUNS):
    """
    Run local_beam_search `num_runs` times and return summary statistics.

    Returns a dict with keys: mean_steps, std_steps, mean_value, std_value.
    """
    steps_list = []
    values_list = []
    for _ in range(num_runs):
        _, _, value, steps = local_beam_search(func, step, beam_width)
        steps_list.append(steps)
        values_list.append(value)

    return {
        "mean_steps": statistics.mean(steps_list),
        "std_steps": statistics.pstdev(steps_list),
        "mean_value": statistics.mean(values_list),
        "std_value": statistics.pstdev(values_list),
    }


def print_table(title, rows, headers):
    """Simple text-table printer for reporting results (part a/b)."""
    print(f"\n{title}")
    col_widths = [max(len(str(h)), *(len(f'{r[i]:.4f}' if isinstance(r[i], float) else str(r[i])) for r in rows))
                  for i, h in enumerate(headers)]
    header_line = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    print(header_line)
    print("-" * len(header_line))
    for row in rows:
        cells = [f"{v:.4f}".ljust(w) if isinstance(v, float) else str(v).ljust(w)
                 for v, w in zip(row, col_widths)]
        print(" | ".join(cells))


if __name__ == "__main__":
    functions = {"f1": f1, "f2": f2}

    # Part (a): hill climbing over step sizes
    for fname, func in functions.items():
        rows = []
        for step in STEP_SIZES:
            stats = run_hill_climbing_experiment(func, step)
            rows.append((step, stats["mean_steps"], stats["std_steps"],
                         stats["mean_value"], stats["std_value"]))
        print_table(
            f"Hill Climbing on {fname}",
            rows,
            ["step_size", "mean_steps", "std_steps", "mean_value", "std_value"],
        )

    # Part (b): local beam search over beam widths
    # TODO: pick a step size (or loop over STEP_SIZES too) to pair with
    # each beam width, consistent with how you want to present results.
    for fname, func in functions.items():
        rows = []
        for width in BEAM_WIDTHS:
            stats = run_beam_search_experiment(func, step=0.1, beam_width=width)
            rows.append((width, stats["mean_steps"], stats["std_steps"],
                         stats["mean_value"], stats["std_value"]))
        print_table(
            f"Local Beam Search on {fname}",
            rows,
            ["beam_width", "mean_steps", "std_steps", "mean_value", "std_value"],
        )
