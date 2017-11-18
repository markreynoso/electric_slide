"""Algorithms for the AI of solving a sliding puzzle."""

from electric_slide.scripts.priority_q import Node, PriorityQ


def manhattan_distance(board_state, size=3):
    """Sum up the manhattan distance of all numbers in the board."""
    diff = 0
    for y in range(size):
        for x in range(size):
            idx = board_state[y][x] - 1
            if idx != 8:
                diff += abs(idx % size - x) + abs(idx // size - y)
    return diff


def a_star(starting_state, heuristic=manhattan_distance):
    """Find a solution path by exploring possible boards.

    Based on heuristic value and path length.
    """
    available = PriorityQ()
    curr = Node(starting_state, None, None)
    visited = [curr]
    while heuristic(curr.state):  # heuristic is non-zero when unsolved
        for move in curr.legal_moves():
            move_state = curr.board.practice_slide(move)
            node = Node(move_state, move, curr)
            value = heuristic(node.state) + len(node.path())
            if available.priority(node) is None and node not in visited:
                available.push(node, value)
            elif node not in visited:
                p = available.priority(node)
                if p > value:
                    available.remove(node, p)
                    available.push(node, value)
        curr = available.pop()
        visited.append(curr)
    return list(reversed(curr.path()))  # heuristic is zero, i.e. solved


def greedy_pure_search(starting_state, heuristic=manhattan_distance):
    """Find solution path by exploring possible boards.

    Based on heuristic value only.
    """
    available = PriorityQ()
    curr = Node(starting_state, None, None)
    visited = [curr]
    while heuristic(curr.state):  # heuristic is non-zero when unsolved
        for move in curr.legal_moves():
            move_state = curr.board.practice_slide(move)
            node = Node(move_state, move, curr)
            value = heuristic(node.state)
            if available.priority(node) is None and node not in visited:
                available.push(node, value)
            elif node not in visited:
                p = available.priority(node)
                if p > value:
                    available.remove(node, p)
                    available.push(node, value)
        curr = available.pop()
        visited.append(curr)
    return list(reversed(curr.path()))  # heuristic is zero, i.e. solved
