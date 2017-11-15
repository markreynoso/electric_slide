"""Comparator function for various solving methods."""

from electric_slide.scripts.algorithm import a_star, greedy_pure_search
from board import Board
from copy import deepcopy
import time
import json

one_of_each = {"[[1, 2, 3], [4, 5, 6], [7, 9, 8]]": 1, "[[1, 2, 9], [4, 5, 3], [7, 8, 6]]": 2, "[[1, 2, 3], [4, 8, 5], [7, 9, 6]]": 3, "[[9, 2, 3], [1, 4, 5], [7, 8, 6]]": 4, "[[1, 5, 2], [9, 4, 3], [7, 8, 6]]": 5, "[[1, 2, 3], [5, 6, 8], [4, 7, 9]]": 6, "[[1, 2, 3], [7, 4, 9], [5, 8, 6]]": 7, "[[1, 3, 9], [7, 2, 6], [5, 4, 8]]": 8, "[[1, 9, 5], [4, 3, 6], [7, 2, 8]]": 9, "[[1, 6, 2], [5, 7, 3], [4, 8, 9]]": 10, "[[1, 6, 2], [4, 8, 9], [7, 3, 5]]": 11, "[[7, 3, 9], [2, 1, 5], [8, 4, 6]]": 12, "[[2, 3, 4], [1, 7, 9], [8, 6, 5]]": 13, "[[1, 2, 3], [6, 7, 4], [9, 5, 8]]": 14, "[[7, 5, 3], [9, 1, 6], [2, 4, 8]]": 15, "[[7, 4, 1], [3, 9, 2], [5, 6, 8]]": 16, "[[1, 6, 2], [5, 4, 3], [8, 9, 7]]": 17, "[[2, 5, 9], [4, 1, 6], [7, 3, 8]]": 18, "[[2, 6, 8], [7, 3, 5], [4, 9, 1]]": 19, "[[3, 4, 1], [5, 7, 6], [9, 2, 8]]": 20, "[[5, 2, 4], [9, 3, 8], [6, 1, 7]]": 21, "[[9, 6, 3], [1, 8, 7], [5, 2, 4]]": 22, "[[5, 6, 4], [2, 8, 1], [7, 9, 3]]": 23, "[[6, 4, 5], [7, 9, 8], [3, 2, 1]]": 24, "[[5, 2, 4], [7, 8, 6], [3, 9, 1]]": 25, "[[5, 6, 4], [7, 8, 3], [2, 1, 9]]": 26, "[[5, 9, 7], [4, 8, 6], [1, 3, 2]]": 27, "[[8, 7, 9], [4, 2, 6], [1, 3, 5]]": 28, "[[8, 4, 7], [9, 6, 2], [3, 5, 1]]": 29, "[[6, 4, 7], [3, 5, 2], [9, 8, 1]]": 30, "[[8, 6, 7], [2, 5, 4], [3, 9, 1]]": 31}


def comparator(starting_state):
    """."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    b = Board()

    complexity = state_almanac[str(starting_state)]

    state_copy = deepcopy(starting_state)

    a_star_start_time = time.time()
    a_star_moves = len(a_star(starting_state)) - 1
    a_star_solve_time = round(((time.time() - a_star_start_time) * 1000), 1)

    with open("electric_slide/data/a_star_data.json") as f:
        d = json.load(f)

    d.setdefault(complexity, {"time": a_star_solve_time, "moves": a_star_moves})

    with open('electric_slide/data/a_star_data.json', 'w') as file:
        json.dump(d, file)

    tree_start_time = time.time()
    tree_moves = b.solve(starting_state, state_almanac)
    tree_solve_time = round(((time.time() - tree_start_time) * 1000), 1)

    with open("electric_slide/data/tree_data.json") as f:
        d = json.load(f)

    d.setdefault(complexity, {"time": tree_solve_time, "moves": tree_moves})

    with open('electric_slide/data/tree_data.json', 'w') as file:
        json.dump(d, file)

    greedy_start_time = time.time()
    greedy_moves = len(greedy_pure_search(state_copy)) - 1
    greedy_solve_time = round(((time.time() - greedy_start_time) * 1000), 1)

    with open("electric_slide/data/greedy_data.json") as f:
        d = json.load(f)

    d.setdefault(complexity, {"time": greedy_solve_time, "moves": greedy_moves})

    with open('electric_slide/data/greedy_data.json', 'w') as file:
        json.dump(d, file)

    return "\n\nComplexity: {}\n\n Tree Time: {} ms\n Tree Moves: {}\n\n A* Time: {} ms\n A* Moves: {}\n\n Greedy Time: {} ms\n Greedy Moves: {}\n\n".format(complexity, tree_solve_time, tree_moves, a_star_solve_time, a_star_moves, greedy_solve_time, greedy_moves)

if __name__ == "__main__":
    one_of_each_complexity = list(one_of_each)

    for state in one_of_each_complexity:
        print(comparator(json.loads(state)))

    # a = json.loads(choice(list(state_almanac)))
    # print(a)

    # print(comparator(a))

    # print(comparator([[6, 4, 7], [8, 5, 9], [3, 2, 1]])) this is a 31
