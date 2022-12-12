import matplotlib.pyplot as plt
import networkx as nx
import networkx.exception

with open('input12.txt') as file:
    input = file.read().splitlines()    # open without /n

heightmap = [[char for char in line] for line in input]

# search for start and end points for first part and all lowest points for second part
start, end, lowest_points = [], [], []

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        elevation = heightmap[i][j]
        if elevation == 'S':
            start.append(i)
            start.append(j)
            heightmap[i][j] = 'a'
        elif elevation == 'E':
            end.append(i)
            end.append(j)
            heightmap[i][j] = 'z'
        if heightmap[i][j] == 'a':
            lowest_points.append(str(i) + '|' + str(j))

# transform characters into ascii values
heightmap = [[ord(value) for value in line] for line in heightmap]

# initiate graph
graph = nx.DiGraph()

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        node_name = str(i) + '|' + str(j)
        graph.add_node(node_name, elevation=heightmap[i][j])

# add edges
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        current, current_node_name = heightmap[i][j], str(i) + '|' + str(j)
        if j + 1 < len(heightmap[0]):
            right, right_node_name = heightmap[i][j + 1], str(i) + '|' + str(j + 1)
            if right - current <= 1:
                graph.add_edge(current_node_name, right_node_name)
        if j - 1 >= 0:
            left, left_node_name = heightmap[i][j - 1], str(i) + '|' + str(j - 1)
            if left - current <= 1:
                graph.add_edge(current_node_name, left_node_name)
        if i + 1 < len(heightmap):
            down, down_node_name = heightmap[i + 1][j], str(i + 1) + '|' + str(j)
            if down - current <= 1:
                graph.add_edge(current_node_name, down_node_name)
        if i - 1 >= 0:
            up, up_node_name = heightmap[i - 1][j], str(i - 1) + '|' + str(j)
            if up - current <= 1:
                graph.add_edge(current_node_name, up_node_name)


def puzzle1():
    start_node_name = str(start[0]) + '|' + str(start[1])
    end_node_name = str(end[0]) + '|' + str(end[1])
    shortest_path_length = nx.shortest_path_length(graph, start_node_name, end_node_name)

    print('shortest path length from start to end:', shortest_path_length)


def puzzle2():
    end_node_name = str(end[0]) + '|' + str(end[1])
    shortest_path_length = 1000

    for low_point in lowest_points:
        try:
            path_length = nx.shortest_path_length(graph, low_point, end_node_name)
            shortest_path_length = min(shortest_path_length, path_length)
        except networkx.exception.NetworkXNoPath:
            continue    # why is there no path to be found for some nodes?!

    print('shortest path length from one of the lowest points to end:', shortest_path_length)


puzzle1()
puzzle2()
