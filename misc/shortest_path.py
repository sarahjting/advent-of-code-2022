from collections import defaultdict, deque

# bfs better for shortest path
def shortest_path(graph, src, dst):
    queue = deque([(src, 0)])
    visited_nodes = {}

    while len(queue) > 0:
        current_node, current_path_length = queue.popleft()
        if current_node not in visited_nodes or visited_nodes[current_node] > current_path_length:
            visited_nodes[current_node] = current_path_length
            queue.extend([(neighbor, current_path_length + 1) for neighbor in graph[current_node]])

    return visited_nodes[dst] if dst in visited_nodes else None

def build_graph(edges):
    graph = defaultdict(lambda:[])
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

edges = [
    ('w', 'x'),
    ('x', 'y'),
    ('y', 'z'),
    ('w', 'v'),
    ('v', 'z')
]

graph = build_graph(edges)
print(shortest_path(graph, 'w', 'z'))