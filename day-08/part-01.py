def count_visible(matrix):
    memo = {}
    mark_visible_top(matrix, memo)
    mark_visible_bottom(matrix, memo)
    mark_visible_left(matrix, memo)
    mark_visible_right(matrix, memo)
    return sum(memo.values())

def mark_visible_top(matrix, memo):
    for r in range(0, len(matrix)):
        current_max = -1
        for c in range(0, len(matrix[r])):
            if (c, r) not in memo or not memo[c, r]:
                memo[c, r] = matrix[c][r] > current_max
            current_max = max(current_max, matrix[c][r])

def mark_visible_bottom(matrix, memo):
    for r in reversed(range(0, len(matrix))):
        current_max = -1
        for c in reversed(range(0, len(matrix[r]))):
            if (c, r) not in memo or not memo[c, r]:
                memo[c, r] = matrix[c][r] > current_max
            current_max = max(current_max, matrix[c][r])

def mark_visible_left(matrix, memo):
    for r in range(0, len(matrix)):
        current_max = -1
        for c in range(0, len(matrix[r])):
            if (r, c) not in memo or not memo[r, c]:
                memo[r, c] = matrix[r][c] > current_max
            current_max = max(current_max, matrix[r][c])

def mark_visible_right(matrix, memo):
    for r in reversed(range(0, len(matrix))):
        current_max = -1
        for c in reversed(range(0, len(matrix[r]))):
            if (r, c) not in memo or not memo[r, c]:
                memo[r, c] = matrix[r][c] > current_max
            current_max = max(current_max, matrix[r][c])

with open('input') as file:
    trees_visible = 0
    matrix = []
    for line in file:
        matrix.append([int(x) for x in list(line.strip('\n'))])

    print(count_visible(matrix))
