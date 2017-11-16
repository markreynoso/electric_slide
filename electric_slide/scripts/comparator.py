"""Comparator function for various solving methods."""
from electric_slide.scripts.algorithm import a_star, greedy_pure_search

from electric_slide.scripts.board import Board

# from copy import deepcopy
from random import sample
import time
import json

# one_of_each = {"[[1, 2, 3], [4, 5, 6], [7, 9, 8]]": 1, "[[1, 2, 9], [4, 5, 3], [7, 8, 6]]": 2, "[[1, 2, 3], [4, 8, 5], [7, 9, 6]]": 3, "[[9, 2, 3], [1, 4, 5], [7, 8, 6]]": 4, "[[1, 5, 2], [9, 4, 3], [7, 8, 6]]": 5, "[[1, 2, 3], [5, 6, 8], [4, 7, 9]]": 6, "[[1, 2, 3], [7, 4, 9], [5, 8, 6]]": 7, "[[1, 3, 9], [7, 2, 6], [5, 4, 8]]": 8, "[[1, 9, 5], [4, 3, 6], [7, 2, 8]]": 9, "[[1, 6, 2], [5, 7, 3], [4, 8, 9]]": 10, "[[1, 6, 2], [4, 8, 9], [7, 3, 5]]": 11, "[[7, 3, 9], [2, 1, 5], [8, 4, 6]]": 12, "[[2, 3, 4], [1, 7, 9], [8, 6, 5]]": 13, "[[1, 2, 3], [6, 7, 4], [9, 5, 8]]": 14, "[[7, 5, 3], [9, 1, 6], [2, 4, 8]]": 15, "[[7, 4, 1], [3, 9, 2], [5, 6, 8]]": 16, "[[1, 6, 2], [5, 4, 3], [8, 9, 7]]": 17, "[[2, 5, 9], [4, 1, 6], [7, 3, 8]]": 18, "[[2, 6, 8], [7, 3, 5], [4, 9, 1]]": 19, "[[3, 4, 1], [5, 7, 6], [9, 2, 8]]": 20, "[[5, 2, 4], [9, 3, 8], [6, 1, 7]]": 21, "[[9, 6, 3], [1, 8, 7], [5, 2, 4]]": 22, "[[5, 6, 4], [2, 8, 1], [7, 9, 3]]": 23, "[[6, 4, 5], [7, 9, 8], [3, 2, 1]]": 24, "[[5, 2, 4], [7, 8, 6], [3, 9, 1]]": 25, "[[5, 6, 4], [7, 8, 3], [2, 1, 9]]": 26, "[[5, 9, 7], [4, 8, 6], [1, 3, 2]]": 27, "[[8, 7, 9], [4, 2, 6], [1, 3, 5]]": 28, "[[8, 4, 7], [9, 6, 2], [3, 5, 1]]": 29, "[[6, 4, 7], [3, 5, 2], [9, 8, 1]]": 30, "[[8, 6, 7], [2, 5, 4], [3, 9, 1]]": 31}


def record_solution_stats(file, solver, starting_state, complexity, almanac=None):
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


# def comparator(starting_state):
#     """Compare the time and moves each algoithm takes to solve the same board."""
#     with open("electric_slide/data/state_almanac_data.json") as f:
#         state_almanac = json.load(f)

#     b = Board()

#     complexity = state_almanac[str(starting_state)]

#     state_copy = deepcopy(starting_state)

#     a_star_data = record_solution_stats('a_star_data.json', a_star,
#                                         starting_state, complexity)
#     a_star_solve_time, a_star_moves = a_star_data

#     tree_data = record_solution_stats('tree_data.json', b.solve, starting_state,
#                                       complexity, state_almanac)
#     tree_solve_time, tree_moves = tree_data

#     greedy_data = record_solution_stats('greedy_data.json', greedy_pure_search,
#                                         state_copy, complexity)
#     greedy_solve_time, greedy_moves = greedy_data

#     return """

# Complexity: {}

#  Tree Time: {} ms
#  Tree Moves: {}

#  A* Time: {} ms
#  A* Moves: {}

#  Greedy Time: {} ms
#  Greedy Moves: {}

#  """.format(complexity, tree_solve_time, tree_moves, a_star_solve_time,
#             a_star_moves, greedy_solve_time, greedy_moves)


def diversify_state_sampling(file, solver, complexity, almanac, tree=False):
    """Record the time and moves a solver takes for a random set of states."""
    states = list(filter(lambda state: almanac[state] == complexity, almanac))
    rand_states = sample(states, min(10, len(states)))
    for state in rand_states:
        state = json.loads(state)
        if tree:
            delta_t, moves = record_solution_stats(file, solver, state, complexity, almanac)
        else:
            delta_t, moves = record_solution_stats(file, solver, state, complexity)
        print('\n {solver} Time: {} ms\
              \n {solver} Moves: {}'.format(delta_t, moves, solver=solver.__name__))


def diversify_comparator():
    """Compare the time and moves each algoithm takes to solve the same board."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    b = Board()

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('greedy_data.json', greedy_pure_search, c, state_almanac)

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('tree_data.json', b.solve, c, state_almanac, True)

    for c in range(32):
        print('\nComplexity: {}'.format(c))
        diversify_state_sampling('a_star_data.json', a_star, c, state_almanac)


if __name__ == "__main__":
    # one_of_each_complexity = list(one_of_each)

    # for _ in range(10):
    #     for state in one_of_each_complexity:
    #         print(comparator(json.loads(state)))

    diversify_comparator()
