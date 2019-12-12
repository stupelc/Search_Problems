from others.node import Node
from others.priority_queue import PriorityQueue
from others.roads import road


# UCS algorithm finds a was from source to target in the minimal cost
def find_ucs_rout(source, target, g, h=None):
    node = Node(road[source])
    frontier = PriorityQueue(lambda node: node.path_cost)  # Priority Queue
    frontier.append(node)
    closed_list = set()
    path = []

    while frontier:
        #if len(closed_list) % 1000 == 0:
         #   print(f'size of closed list:{len(closed_list)}')
        node = frontier.pop()

        if target == node.state.index:
            return node.solution()

        closed_list.add(node.state.index)
        list_nodes = []
        list_nodes = node.expandNode(node, g)

        for child in list_nodes:
            # childNode = Node(child.target, node, None, node.path_cost + g(child))
            if child not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and g(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)

    return None