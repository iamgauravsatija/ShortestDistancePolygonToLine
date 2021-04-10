import math 

class vertex:
    def __init__(self, x_coordinate, y_coordinate, index_val):
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
        numerator = self.x*a + self.y*b - c
        denominator = math.sqrt( (a*a) + (b*b) ) 
        
        if numerator < 0:
            numerator = -1*numerator
        
        return int(numerator/denominator)


class lineClass:
    def __init__(self, a_value, b_value, c_value):
        self.a = a_value
        self.b = b_value
        self.c = c_value
    
    def getValues(self):
        return self.a, self.b, self.c
    

def binarySearchDist(left_vertex, middle_vertex, right_vertex, line_given, polygon_dict):
    # check if dist_left == dist_right and dist_left < dist_mid
        # return
    # check which two are min
    # reassign left and right vertex
    # if right & left are index away
    #    If left < right and mid < right
    #     New_mid_index = left index + midindex // 2
    #     New_ver = dict[new_index]
    #     BSearch( left, new_ver, mid)

    #     Elif  right < left and mid < left
    #     New_mid_index = midindex + right index // 2
    #     New_ver = dict[new_index]
    #     BSearch( mid , new_ver, mid)

    if left_vertex.getIndex() == right_vertex.getIndex() or left_vertex.getIndex() == middle_vertex.getIndex():
        return left_vertex.getDistance(line_given)

    
    if right_vertex.getIndex() == middle_vertex.getIndex():
        return right_vertex.getDistance(line_given)
    

    dist_left  = left_vertex.getDistance(line_given)
    dist_right = right_vertex.getDistance(line_given)
    dist_mid   = middle_vertex.getDistance(line_given)

    if dist_left < dist_right:# and dist_mid < dist_right:
        new_med_index = (left_vertex.getIndex() + middle_vertex.getIndex()) // 2
        new_ver = polygon_dict[int(new_med_index)]
        return binarySearchDist(left_vertex, new_ver, middle_vertex, line_given, polygon_dict)
    
    elif dist_right < dist_left:# and dist_mid < dist_left:
        new_med_index = (right_vertex.getIndex() + middle_vertex.getIndex()) // 2
        print("Index: ", right_vertex.getIndex(),"-", middle_vertex.getIndex(), "-", new_med_index)
        new_ver = polygon_dict[int(new_med_index)]
        return binarySearchDist(middle_vertex, new_ver, right_vertex, line_given, polygon_dict)

# def checkIfShortest(vertex_given, polygon_dict):
    #     keys_list = list(polygon_dict.keys())
    #     vals_list = list(polygon_dict.values())
    #     index_local = keys_list[vals_list.index(vertex_given)]
        
    #     index_below = 0
    #     index_above = 0

    #     if index_local == 0:
    #         index_below = len(keys_list) - 1
    #     else: 
    #         index_below = index_local - 1
        
    #     if index_local == len(keys_list) - 1:
    #         index_above = 0
    #     else:
    #         index_above = index_local + 1


def calculateShortestDistance(number_of_vertices, polygon_dict, line_given):
    # let's take 4 vertices in the polygon
        # vertex_n1 = polygon_dict[0]
        # vertex_n2 = polygon_dict[number_of_vertices/3]
        # vertex_n3 = polygon_dict[2*number_of_vertices/3]
        # vertex_n4 = polygon_dict[number_of_vertices-1]

        # dist_n1 = vertex_n1.getDistance(line_given)
        # dist_n2 = vertex_n2.getDistance(line_given)
        # dist_n3 = vertex_n3.getDistance(line_given)
        # dist_n4 = vertex_n4.getDistance(line_given)
        
        # dist_list = [dist_n1, dist_n2, dist_n3, dist_n4]

        # min_distance = 0
        
        # if dist_n1 == min(dist_list):
        #     min_distance = binarySearchDist(vertex_n2, vertex_n3, vertex_n4)
        # elif dist_n2 == min(dist_list):
        #     min_distance = binarySearchDist(vertex_n2, vertex_n3, vertex_n4)
        # elif dist_n3 == min(dist_list):
        #     min_distance = binarySearchDist(vertex_n2, vertex_n3, vertex_n4)
        # elif dist_n4 == min(dist_list):
        #     min_distance = binarySearchDist(vertex_n2, vertex_n3, vertex_n4)

    vertex_left = polygon_dict[0]
    vertex_mid = polygon_dict[int(number_of_vertices/2)]
    vertex_right = polygon_dict[number_of_vertices-1]

    vertex_list = [vertex_left, vertex_mid, vertex_right]


    dist_left = vertex_left.getDistance(line_given)
    dist_mid = vertex_mid.getDistance(line_given)
    dist_right = vertex_right.getDistance(line_given)

    # check if current node is not the closest one

        # for vertex_itr in vertex_list:
        #     if checkIfShortest(vertex_itr):
        #         return vertex_itr.getDistance(line_given, polygon_dict)
    print("Reached: ", dist_left, "-", dist_mid, "-", dist_right)
    if dist_left == dist_right and dist_left < dist_mid:
        print("YUP")
        return dist_left
    print("NOPE")
    # return "BOOM"
    return binarySearchDist(vertex_left, vertex_mid, vertex_right, line_given, polygon_dict )
    
    

filename = "input.txt"  # Change the input file path here


file = open(filename, "r")

lines = file.readlines()

polygon_dict = {}


vertex_index = 0

number_of_vertices = 0
line_given = 0
for line in lines:
    if number_of_vertices == 0:
        number_of_vertices = int(line)
    
    elif vertex_index < number_of_vertices:
        line = line.split(" ")
        new_vertex = vertex(int(line[0]), int(line[1]), vertex_index)
        polygon_dict[vertex_index] = new_vertex
        vertex_index += 1
    
    else: 
        line = line.split(" ")
        line_given = lineClass(int(line[0]), int(line[1]), int(line[2]))

print("Dist:", calculateShortestDistance(number_of_vertices, polygon_dict, line_given))    
    