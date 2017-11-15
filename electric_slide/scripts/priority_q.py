"""A priority queue of board states for A*."""
from electric_slide.scripts.board import PracticeBoard


class Node(object):
    """Node for the A* algorithm."""

    def __init__(self, state, move, prev):
        """Create a new Node.

        state: list, nxn lists of the current board state
        move: tuple, the move that caused the state
        prev: Node, the node before the current node
        """
        self.move = move
        self.prev = prev
        self.board = PracticeBoard(state)

    @property
    def state(self):
        """Get the state of the board after the the Node's move."""
        return self.board.practice_state

    def path(self):
        """Get the path leading up to the current Node."""
        curr = self
        p = []
        while curr:
            p.append(curr.state)
            curr = curr.prev
        return p

    def __eq__(self, node):
        """Overwrite the equality function for Node.

        Nodes with the same board state are equivalent.
        """
        return isinstance(node, Node) and self.state == node.state

    def legal_moves(self):
        """Determine the legal moves for a board state."""
        return self.board.determine_legal_moves()


class PriorityQ(object):
    """A priority queue where first out is lowest priority."""

    def __init__(self):
        """Create a new priority queue."""
        self.values = {}

    def push(self, item, priority):
        """Add a new item to the queue."""
        self.values.setdefault(priority, [])
        self.values[priority].append(item)

    def pop(self):
        """Remove the highest prioirty item from the queue."""
        min_p = min(self.values)
        result = self.values[min_p].pop()
        if not self.values[min_p]:
            del self.values[min_p]
        return result

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
        if not self.values[priority]:
            del self.values[priority]
