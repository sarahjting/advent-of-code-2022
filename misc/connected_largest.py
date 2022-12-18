from collections import deque

def connected_largest(graph):
    visited_nodes = set()

    current_max = 0
    for (current_node, neighbors) in graph.items():
        current_max = max(current_max, count_connected_nodes(graph, current_node, visited_nodes))

    return current_max

def count_connected_nodes(graph, current_node, visited_nodes):
    if current_node in visited_nodes:
        return 0

    count = 1

    visited_nodes.add(current_node)
    for neighbor in graph[current_node]:
        count += count_connected_nodes(graph, neighbor, visited_nodes)

    return count

graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}

print(connected_largest(graph))