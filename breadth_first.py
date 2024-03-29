from collections import deque


class GraphNode(object):
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


def find_node(node, value):
    """Given a node in a directed graph (that may contain cycles) and a value,
    finds the node with the corresponding value via breadth-first search and
    returns it.


    Without cycles:

    >>> node_a = GraphNode("a")
    >>> node_b = GraphNode("b")
    >>> node_c = GraphNode("c")
    >>> node_d = GraphNode("d")
    >>> node_e = GraphNode("e")
    >>> node_f = GraphNode("f")
    >>> node_g = GraphNode("g")

    >>> node_a.children = [node_b, node_c]
    >>> node_b.children = [node_d, node_e, node_f]
    >>> node_c.children = [node_g]

    >>> (find_node(node_a, "g")).data == "g"
    True

    >>> find_node(node_a, "nope")
    'Node not found.'


    With cycles:

    >>> node_a = GraphNode("a")
    >>> node_b = GraphNode("b")
    >>> node_c = GraphNode("c")
    >>> node_d = GraphNode("d")
    >>> node_e = GraphNode("e")
    >>> node_f = GraphNode("f")
    >>> node_g = GraphNode("g")

    >>> node_a.children = [node_b, node_c, node_a]
    >>> node_b.children = [node_d, node_e, node_f, node_a]
    >>> node_c.children = [node_g]

    >>> (find_node(node_a, "g")).data == "g"
    True

    >>> find_node(node_a, "nope")
    'Node not found.'

    """

    seen = set()
    queue = deque()

    queue.append(node)

    while queue:

        current = queue.popleft()

        if current not in seen:
            if current.data == value:
                return current
            else:
                seen.add(current)
                queue.extend(current.children)

    return "Node not found."

if __name__ == "__main__":
    import doctest
    doctest.testmod()
