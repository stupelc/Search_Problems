import csv
import os
import matplotlib.pyplot as plt

import main
from algorithms import astarAlgorithm
from others.node import Node
from others.roads import road
from others.heuristic import Heuristic
from ways import draw

plt.axis('equal')
hurLon, realLat = [], []


# write the way the algorithm did in this case
def write_results_astar():
    with open("problems.csv", 'r') as f:
        filereader = csv.reader(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(os.path.join("results", "AStarRuns.txt"), 'w') as fw:
            for row in filereader:
                path = main.find_astar_route(int(row[0]), int(row[1]))
                print(' '.join(str(j.state.index) for j in path))
                for j in path:
                    fw.writelines(' ' + str(j.state.index))
                fw.writelines("\n")


# create the graph that shows the heuristic and real time
def createGraph():
    with open("problems.csv", 'r') as f:
        filereader = csv.reader(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(os.path.join("results", "AStarRuns.txt"), 'w') as fw:
            for row in filereader:
                source = int(row[0])
                nodeSource = Node(road[source])
                target = int(row[1])
                path = main.find_astar_route(source, target)
                print(' '.join(str(j.state.index) for j in path))

                hurTime = Heuristic(target).hur(nodeSource)
                realTime = path[-1].path_cost
                hurLon.append(hurTime)
                realLat.append(realTime)

                fw.writelines(str(hurTime) + ',' + str(realTime))
                fw.writelines("\n")

                plt.plot(hurLon, realLat, 'bo')

        plt.show()


# function that drows the way we did according to A*
def saveWay():
    counter = 1
    with open("problems.csv", 'r') as f:
        filereader = csv.reader(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in filereader:
            if counter > 10:
                break;
            source = int(row[0])
            target = int(row[1])
            path = main.find_astar_route(source, target)
            print(' '.join(str(j.state.index) for j in path))

            draw.plot_path(road, path)
            fileName = 'solutions_img/' + str(source) + '_' + str(target) + '.png'
            plt.savefig(fileName)

            plt.show()
            counter = counter + 1

