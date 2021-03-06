# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author:  @iamgauravsatija on Github                                       #
# I would like to give credit to the following courses for helping me:      #
#   Geeksforgeeks.com                                                       #
#   Youtube.com                                                             #
#   Stackoverflow.com                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import math


class vertex:
    """[summary]"""

    def __init__(self, x_coordinate: int, y_coordinate: int, index_val: int) -> None: # ignore for flake
        """[summary]

        Args:
            x_coordinate (int): [description]
            y_coordinate (int): [description]
            index_val (int): [description]
        """
        self.x = x_coordinate
        self.y = y_coordinate
        self.index_val = index_val

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getIndex(self):
        return self.index_val

    def getDistance(self, line_local):
        a, b, c = line_local.getValues()
        numerator = self.x * a + self.y * b - c
        denominator = math.sqrt((a * a) + (b * b))

        if numerator < 0:
            numerator = -1 * numerator

        return int(numerator / denominator)


class lineClass:
    def __init__(self, a_value, b_value, c_value):
        self.a = a_value
        self.b = b_value
        self.c = c_value

    def getValues(self):
        return self.a, self.b, self.c


def binarySearchDist(
    left_vertex, middle_vertex, right_vertex, line_given, polygon_dict
):

    if left_vertex.getDistance(line_given) == right_vertex.getDistance(
        line_given
    ) and left_vertex.getDistance(line_given) == middle_vertex.getDistance(line_given):
        return left_vertex

    # if right_vertex.getIndex() == middle_vertex.getIndex():
    #     return right_vertex.getDistance(line_given)

    dist_left = left_vertex.getDistance(line_given)
    dist_right = right_vertex.getDistance(line_given)

    if dist_left < dist_right:
        new_med_index = (left_vertex.getIndex() + middle_vertex.getIndex()) // 2
        new_ver = polygon_dict[int(new_med_index)]
        return binarySearchDist(
            left_vertex, new_ver, middle_vertex, line_given, polygon_dict
        )

    elif dist_right < dist_left:
        new_med_index = ((right_vertex.getIndex() + middle_vertex.getIndex()) // 2) + 1
        new_ver = polygon_dict[int(new_med_index)]
        return binarySearchDist(
            middle_vertex, new_ver, right_vertex, line_given, polygon_dict
        )


def calculateShortestDistance(number_of_vertices, polygon_dict, line_given):
    vertex_left = polygon_dict[0]
    vertex_mid = polygon_dict[int(number_of_vertices / 2)]
    vertex_right = polygon_dict[number_of_vertices - 1]

    dist_left = vertex_left.getDistance(line_given)
    dist_mid = vertex_mid.getDistance(line_given)
    dist_right = vertex_right.getDistance(line_given)

    # check if current node is not the closest one
    if dist_left == dist_right and dist_left < dist_mid:
        return dist_left

    return binarySearchDist(
        vertex_left, vertex_mid, vertex_right, line_given, polygon_dict
    )
