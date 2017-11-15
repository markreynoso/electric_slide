"""Comparator function for various solving methods."""

from electric_slide.scripts.board import Board
from electric_slide.scripts.algorithm import a_star, greedy_pure_search
import time
import json


def comparator(starting_state):
    """."""
    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    b = Board()

    complexity = state_almanac[str(starting_state)]

    a_star_start_time = time.time()
    a_star_moves = len(a_star(starting_state)) - 1
    a_star_solve_time = (time.time() - a_star_start_time) * 1000

    tree_start_time = time.time()
    tree_moves = b.solve(starting_state, state_almanac)
    tree_solve_time = (time.time() - tree_start_time) * 1000

    greedy_start_time = time.time()
    greedy_moves = len(greedy_pure_search(starting_state)) - 1
    greedy_solve_time = (time.time() - greedy_start_time) * 1000

    return "\n\nComplexity: {}\n\n Tree Time: {} ms\n Tree Moves: {}\n\n A* Time: {} ms\n A* Moves: {}\n\n Greedy Time: {} ms\n Greedy Moves: {}\n\n".format(complexity, tree_solve_time, tree_moves, a_star_solve_time, a_star_moves, greedy_solve_time, greedy_moves)

if __name__ == "__main__":
    from random import choice

    with open("electric_slide/data/state_almanac_data.json") as f:
        state_almanac = json.load(f)

    a = json.loads(choice(list(state_almanac)))
    print(a)

    print(comparator(a))

    # print(comparator([[6, 4, 7], [8, 5, 9], [3, 2, 1]])) this is a 31
