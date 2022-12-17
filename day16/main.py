import networkx as nx
import matplotlib.pyplot as plt

with open('input16.txt') as file:
    puzzle_input = file.read().splitlines()    # open without /n

tunnels = []

for i in range(len(puzzle_input)):
    tunnel = []
    tunnel_info = puzzle_input[i].replace('Valve ', '').split(' has flow rate=')
    tunnel_name = tunnel_info[0]
    tunnel.append(tunnel_name)
    tunnel_info[1] = tunnel_info[1].split(';')
    flow_rate = int(tunnel_info[1][0])
    tunnel.append(flow_rate)
    tunnel_info[1][1] = tunnel_info[1][1].split(', ')
    leading_into = [t_info[-2:] for t_info in tunnel_info[1][1]]
    tunnel.append(leading_into)
    tunnels.append(tunnel)

graph = nx.Graph()

for tunnel in tunnels:
    flow_rate = tunnel[1] if tunnel[1] != 0 else ''
    if tunnel[0] == 'AA':
        flow_rate = 'AA'
    graph.add_node(tunnel[0], flow_rate=flow_rate)

for tunnel in tunnels:
    for linked_tunnel in tunnel[2]:
        graph.add_edge(tunnel[0], linked_tunnel)

# draw graph
labels = nx.get_node_attributes(graph, 'flow_rate')
nx.draw(graph, labels=labels)
plt.show()


def find_all_paths(current, necessary, visited, time):
    all_necessary_visited = True
    for necessary_tunnel in necessary:
        if necessary_tunnel not in visited:
            all_necessary_visited = False

    if all_necessary_visited or time >= 30:
        return visited

    paths = []

    linked_tunnels = graph[current]
    for linked_tunnel in linked_tunnels:
        if graph.nodes[linked_tunnel]['flow_rate'] != 0:
            if linked_tunnel not in visited:
                paths.append(find_all_paths(linked_tunnel, necessary, new_visits, time + 2))

        else:
            paths.append(find_all_paths(linked_tunnel, necessary, new_visits, time + 1))

    return paths

# time = 0
# total_released_pressure = 0
# released_pressure_per_minute = 0
# current_tunnel = 'AA'
#
# while time < 30:
#     flow_rate = graph.nodes[current_tunnel]['flow_rate']
#     elapsed_time = 1 if flow_rate == 0 else 2
#     time += elapsed_time
#     if time > 30:
#         break
#     total_released_pressure += elapsed_time * released_pressure_per_minute
#     if flow_rate != 0:
#         released_pressure_per_minute += flow_rate
#
