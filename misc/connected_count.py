from collections import deque

def connected_count(graph):
    visited_nodes = set()
    count = 0

    for (current_node, neighbors) in graph.items():
        if mark_connected_nodes(graph, current_node, visited_nodes):
            count += 1

    return count

def mark_connected_nodes(graph, current_node, visited_nodes):
    if current_node in visited_nodes:
        return False

    visited_nodes.add(current_node)

    for neighbor in graph[current_node]:
        mark_connected_nodes(graph, neighbor, visited_nodes)

    return True

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

print(connected_count(graph))