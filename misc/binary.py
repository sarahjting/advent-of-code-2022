from collections import deque
from math import inf

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def depth_first_values(node):
    stack = [node]
    values = []
    while len(stack) > 0:
        current_node = stack.pop()
        values.append(current_node.data)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return values

def depth_first_values_recursive(node):
    if not node:
        return []

    return [node.data] + depth_first_values_recursive(node.left) + depth_first_values_recursive(node.right)

def depth_first_search(node, needle):
    stack = [node]
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.data == needle:
            return True
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return False

def breadth_first_values(node):
    queue = deque([node])
    values = []
    while len(queue) > 0:
        current_node = queue.popleft()
        values.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return values

def breadth_first_search(node, needle):
    queue = deque([node])
    while len(queue) > 0:
        current_node = queue.popleft()
        if (current_node.data == needle):
            return True
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return False

def binary_sum(node):
    sum = 0
    queue = deque([node])
    while len(queue) > 0:
        current_node = queue.popleft()
        sum += current_node.data
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return sum

def binary_min(node):
    if not node:
        return inf

    return min(node.data, binary_min(node.left), binary_min(node.right))

def max_path(node):
    if not node:
        return 0

    return node.data + max(max_path(node.left), max_path(node.right))

a = Node(1)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depth_first_values(a))
print(depth_first_values_recursive(a))
print(breadth_first_values(a))
print(depth_first_search(a, 1))
print(breadth_first_search(a, 1))
print(binary_sum(a))
print(binary_min(a))
print(max_path(a))
