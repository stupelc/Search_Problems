import main
import csv
import os

def write_results_ucs():
    with open("problems.csv", 'r') as f:
        filereader = csv.reader(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(os.path.join("results", "USCRuns.txt"), 'w') as fw:
            for row in filereader:
                path = main.find_ucs_rout(int(row[0]), int(row[1]))
                print(' '.join(str(j.state.index) for j in path))
                cost = path[len(path) - 1].path_cost
                fw.writelines(' ' + str(cost))
                fw.writelines("\n")

