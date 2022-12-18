from collections import deque

def has_path_bfs(graph, src, dst):
    queue = deque([src])

    while len(queue) > 0:
        current_node = queue.popleft()
        if (current_node == dst):
            return True

        queue.extend(graph[current_node])

    return False

def has_path_dfs(graph, src, dst):
    stack = [src]

    while len(stack) > 0:
        current_node = stack.pop()
        if (current_node == dst):
            return True

        stack.extend(graph[current_node])

    return False

def has_path_dfs_recursive(graph, src, dst):
    if src == dst:
        return True

    for node in graph[src]:
        if has_path_dfs_recursive(graph, node, dst):
            return True

    return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path_dfs_recursive(graph, 'h', 'k'))