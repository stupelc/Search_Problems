from others.roads import road
from ways import graph
from functools import total_ordering

# Node class for each junction from the map
@total_ordering
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, node, f):
        father = road[int(node.state)]
        links = tuple(lnk for lnk in father.links)
        return links

    def expandNode(self, node, f):
        father = node.state
        links = tuple(lnk for lnk in father.links)
        nodes = []
        for link in links:
            nodes.append(Node(road[link.target], node, None, graph.cost_path(link) + f(node)))
        return nodes

    def solution(self):
        return [node for node in self.path()]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __getstate__(self):
        return self.state

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state.index)
