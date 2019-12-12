'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
# this file prints the map_statistics file

from collections import Counter
from collections import namedtuple
from ways import load_map_from_csv


# Return a dictionary containing the desired information
def map_statistics(roads):
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    # Number of links
    numLinks = 0
    for i in range(0, len(roads)):
        numLinks += len(roads[i].links)

    # Outgoing branching factor
    max_links = 0
    min_links = 0
    sum_links = 0
    for i in range(0, len(roads)):
        links_num = len(roads[i].links)
        sum_links += links_num
        if (max_links < links_num):
            max_links = links_num
        if (min_links > links_num):
            min_links = links_num
    avg_links = sum_links / len(roads)

    # Link distance
    max_distance = 0
    min_distance = 0
    sum_distance = 0
    for i in roads:
        for j in roads[i].links:
            sum_distance += j.distance
            if (max_distance < j.distance):
                max_distance = j.distance
            if (min_distance > j.distance):
                min_distance = j.distance
    avg_distance = sum_distance / numLinks

    # Link type histogram
    histogramTypes = []
    for i in roads:
        for j in roads[i].links:
            histogramTypes.append(j.highway_type)

    return {
        'Number of junctions': len(roads),
        'Number of links': numLinks,
        'Outgoing branching factor': Stat(max=max_links, min=min_links, avg=avg_links),
        'Link distance': Stat(max=max_distance, min=min_distance, avg=avg_distance),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': Counter(histogramTypes),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
    print("hello")
