class GraphNode(object):
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


def find(node, value):
    """Given a node in a directed graph that may contain cycles and a value,
    finds the node in the graph with the corresponding value via breadth-first
    search and returns it.

    """
    seen = set([])
    to_check = []

    if node.data == value:
        return node
    else:
        seen.add(node)
        to_check.extend(node.children)

    while to_check:

        current = to_check[0]

        if current not in seen:
            if current.data == value:
                return current
            else:
                seen.add(current)
                to_check.pop(0)
                to_check.extend(current.children)

        else:
            to_check.remove(current)

    return "Node not found."

"""For creating a test graph:

Without cycles:

node_a = GraphNode("a")
node_b = Graphnode("b")
node_c = Graphnode("c")
node_d = GraphNode("d")
node_f = GraphNode("f")
node_e = GraphNode("e")
node_g = GraphNode("g")

node_a.children = [node_b, node_c]
node_b.children = [node_d, node_e, node_f]
node_c.children = [node_g]

Test cases:

find(node_a, "g")
find(node_a, "nope")

With cycles:

node_a = GraphNode("a")
node_b = Graphnode("b")
node_c = Graphnode("c")
node_d = GraphNode("d")
node_f = GraphNode("f")
node_e = GraphNode("e")
node_g = GraphNode("g")

node_a.children = [node_b, node_c, node_a]
node_b.children = [node_d, node_e, node_f, node_a]
node_c.children = [node_g]

Test cases:

find(graph, "g")
find(graph, "nope")

"""
