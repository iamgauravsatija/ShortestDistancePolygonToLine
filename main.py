from src.shortstDistance import calculateShortestDistance, lineClass, vertex


def main():
    filename = "data/input2.txt"  # Change the input file path here
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

    desired_point = calculateShortestDistance(
        number_of_vertices, polygon_dict, line_given
    )
    print("\n")
    print("======================================================\n")
    print("Input file name: ", filename)
    print("Number of Vertices: ", number_of_vertices)
    print(
        "Closest Point on Polygon to Line:    X-",
        desired_point.getX(),
        ", Y-",
        desired_point.getY(),
    )
    print("Distance to the Polygon: ", desired_point.getDistance(line_given))
    print("\n======================================================")
    print("\n")


if __name__ == "__main__":
    main()
