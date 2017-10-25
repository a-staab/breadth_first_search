class Node(object):
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def add_node(self, parent, value, children=None):
        """Given the parent node, children, and value of a new node, creates a
        new node and adds it to the graph."""

        self = Node(value, children)
        parent.children.append(self)


def find(node, value):
    """Given a node in a directed graph (that may contain cycles) and a value,
    finds the node in the graph with the corresponding value via breadth-first
    search and returns it.

    """
    seen = {}
    to_check = []

    if node.data == value:
        return node
    else:
        seen.add(node)
        to_check.extend(node.children)

    while to_check:

        for current in to_check:
            if current not in seen:
                if current.data == value:
                    return current
                else:
                    seen.add(current)
                    to_check.extend(current.children)
            else:
                continue

    return "Node not found."
