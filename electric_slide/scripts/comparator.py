"""Comparator function for various solving methods."""
import json
import time
from random import sample


from electric_slide.scripts.algorithm import a_star, greedy_pure_search
from electric_slide.scripts.board import Board


def record_solution_stats(file, solver, starting_state,
                          complexity, almanac=None):
    """Time how long it takes to get a solution for a given solver."""
    if almanac is None:
        start_time = time.time()
        solution = solver(starting_state)
        solve_time = (time.time() - start_time) * 1000
    else:
        start_time = time.time()
        solution = solver(starting_state, almanac)
        solve_time = (time.time() - start_time) * 1000

    moves = solution if isinstance(solution, int) else len(solution) - 1

    with open("electric_slide/data/" + file) as f:
        d = json.load(f)
    d.setdefault(str(complexity), {"time": [], "moves": []})
    d[str(complexity)]['time'].append(solve_time)
    d[str(complexity)]['moves'].append(moves)

    with open('electric_slide/data/' + file, 'w') as f:
        json.dump(d, f)

    return solve_time, moves


def diversify_state_sampling(file, solver, complexity, almanac, tree=False):  # pragma: no cover
    """Record the time and moves a solver takes for a random set of states."""
    states = list(filter(lambda state: almanac[state] == complexity, almanac))
    rand_states = sample(states, min(10, len(states)))
    for state in rand_states:
        state = json.loads(state)
        if tree:
            delta_t, moves = record_solution_stats(file, solver, state,
                                                   complexity, almanac)
        else:
            delta_t, moves = record_solution_stats(file, solver,
                                                   state, complexity)
        print('\n {solver} Time: {} ms\
              \n {solver} Moves: {}'.format(delta_t, moves,
                                            solver=solver.__name__))


def diversify_comparator():  # pragma: no cover
    """Compare time and moves each algoithm takes to solve the same board."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    b = Board()

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('greedy_data.json', greedy_pure_search,
                                 c, state_almanac)

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('tree_data.json', b.solve, c,
                                 state_almanac, True)

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('a_star_data.json', a_star, c, state_almanac)


if __name__ == "__main__":  # pragma: no cover
    diversify_comparator()
