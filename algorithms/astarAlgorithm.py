from others.node import Node
from others.priority_queue import PriorityQueue
from others.roads import road


def find_astar_route(source, target, g, h=None):
    node = Node(road[source])  # take the first node in the way
    frontier = PriorityQueue(lambda node: node.path_cost)  # enter the node to the priority queue
    frontier.append(node)
    closed_list = set()

    while frontier:
        node = frontier.pop()
        if target == node.state.index:
            return node.solution()

        closed_list.add(node.state.index)
        list_nodes = []
        list_nodes = node.expandNode(node, g)  # adding the neighbors of the node and update the cost

        for child in list_nodes:
            if child not in closed_list and child not in frontier:  # if we didn't visit in the junction already
                frontier.append(child)

            elif child in frontier and (g(child) + h(child)) < frontier[child]:  # if we get to the same junction in less cost
                del frontier[child]
                frontier.append(child)
    return None
