from others.roads import road
from ways import info
from ways import tools


# class for compute the heuristic result for each junction
class Heuristic:

    def __init__(self, target_num):
        self.target = road[target_num]

    def hur(self, curr_source_node):
        a = tools.compute_distance(curr_source_node.state.lat, curr_source_node.state.lon,
                                   self.target.lat, self.target.lon)
        maximum = -1
        for j in range(0, len(info.SPEED_RANGES)):
            if maximum < info.SPEED_RANGES[j][1]:
                maximum = info.SPEED_RANGES[j][1]
        # need to devide it in the max velocity of the road
        return a / maximum
