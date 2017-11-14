"""A priority queue of board states for A*."""
from board import Board


class Node(object):
    """Node for the A* algorithm."""

    def __init__(self, state, move, prev):
        """Create a new Node.

        state: list, nxn lists of the current board state
        move: tuple, the move that caused the state
        prev: Node, the node before the current node
        """
        self.state = state
        self.move = move
        self.prev = prev
        self.board = Board

    def path(self):
        """Get the path leading up to the current Node."""
        curr = self
        p = []
        while curr:
            p.append(self.move)
            curr = curr.prev
        return p

    def __eq__(self, node):
        """Overwrite the equality function for Node.

        Nodes with the same board state are equivalent.
        """
        return isinstance(node, Node) and self.state == node.state

    def legal_moves(self):
        """Determine the legal moves for a board state."""
        flat = [val for row in self.state for val in row]
        empty = flat.index(9)
        coords = (empty % 3 + 1, empty // 3 + 1)
        self.board._determine_legal_moves(coords)
        return self.board.legal_moves


class PriorityQ(object):
    """A priority queue where first out is lowest priority."""

    def __init__(self):
        """Create a new priority queue."""
        self.values = {}

    def push(self, item, priority):
        """Add a new item to the queue."""
        self.values.setdefault(priority, [])
        self.values[priority].append(item)

    def pop(self, item, priority):
        """Remove the highest prioirty item from the queue."""
        return self.values[min(self.values)].pop()

    def priority(self, item):
        """Find the priority of the given item."""
        for p in self.values:
            if item in self.values[p]:
                return p

    def remove(self, item, priority=None):
        """Remove the given item from the queue.

        If given a priority, will only remove from that priority.
        """
        if priority is None:
            priority = self.priority(item)

        self.values[priority].remove(item)
