from algorithms import uscAlogorithm
from algorithms import astarAlgorithm
from algorithms import idastarAlgorithm
from others.heuristic import Heuristic

# the UCS algorithm - call function to find path, and return list of indices
def find_ucs_rout(source, target):
    def g(node):
        return node.path_cost

    return uscAlogorithm.find_ucs_rout(source, target, g)


# the A* algorithm - call function to find path, and return list of indices
def find_astar_route(source, target):
    def g(node):
        return node.path_cost

    return astarAlgorithm.find_astar_route(source, target, g, Heuristic(target).hur)


# the IDA* algorithm - call function to find path, and return list of indices
def find_idastar_route(source, target):
    def g(node):
        return node.path_cost

    return idastarAlgorithm.find_ida_star_route(source, target, g, Heuristic(target).hur)


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
        print(' '.join(str(j.state.index) for j in path))

    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
        print(' '.join(str(j.state.index) for j in path))

    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
        print(' '.join(str(j.state.index) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
