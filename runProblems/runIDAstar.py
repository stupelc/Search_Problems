import csv
import os
import main
from others.node import Node
from others.roads import road
from others.heuristic import Heuristic


# write the way the algorithm did in this case
def write_results_idastar():
    with open("problems.csv", 'r') as f:
        filereader = csv.reader(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(os.path.join("results", "IDAStarRuns.txt"), 'w') as fw:
            counter = 1
            for row in filereader:
                if (counter > 5):
                    break
                source = int(row[0])
                nodeSource = Node(road[source])
                target = int(row[1])
                path = main.find_astar_route(source, target)
                print(' '.join(str(j.state.index) for j in path))

                hurTime = Heuristic(target).hur(nodeSource)
                realTime = path[-1].path_cost

                fw.writelines(str(hurTime) + ',' + str(realTime))
                fw.writelines("\n")
                counter += 1

