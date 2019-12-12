import math
from others.roads import road
from others.node import Node

FOUND = 1
NOT_FOUND = 2


# based on the pseudo-code from: https://en.wikipedia.org/wiki/Iterative_deepening_A*
def find_ida_star_route(source, target, g, h):
    sourceNode = Node(road[source])
    bound = h(sourceNode)
    path = [sourceNode] # current search path
    while 1:
        target = search(path, g, bound, target, h)
        if target == FOUND:
            return path
        if target == math.inf:
            return NOT_FOUND
        bound = target


def search(path, g, bound, target, h):
    node = path[-1]
    f = g(node) + h(node)
    if f > bound:
        return f
    if target == node.state.index:
        return FOUND
    min = math.inf
    list_nodes = node.expandNode(node, g)
    for succ in list_nodes:
        path.append(succ)
        t = search(path, g, bound, target, h)
        if t == FOUND:
            return FOUND
        if t < min:
            min = t
        path.pop()
    return min