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

Test cases:

find(node_a, "g")
find(node_a, "nope")

With a cycle:

graph = GraphNode("a")
graph.add_new_node(graph, "b")
graph.add_new_node(graph, "c")
graph.children[0].add_new_node(graph.children[0], "d")
graph.children[0].add_new_node(graph.children[0], "e")
graph.children[0].add_new_node(graph.children[0], "f")
graph.children[0].make_cycle(graph.children[0], graph)
graph.children[1].add_new_node(graph.children[1], "c")
graph.children[1].children[0].add_new_node(graph.children[1].children[0], "g")

Test cases:

find(graph, "g")
find(graph, "moon")

"""