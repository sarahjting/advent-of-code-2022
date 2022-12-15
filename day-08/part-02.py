def get_max_scenic_score(matrix):
    scenic_scores = get_scenic_scores(matrix)
    return max(scenic_scores.values())

def get_scenic_scores(matrix):
    scenic_scores = {}
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix)):
            scenic_scores[(r, c)] = get_scenic_score(matrix, r, c)
    return scenic_scores

def get_scenic_score(matrix, r, c):
    current_height = matrix[r][c]

    up_score = 0
    if r > 0:
        for current_row in reversed(range(0, r)):
            up_score += 1
            if (matrix[current_row][c] >= current_height):
                break

    down_score = 0
    if r < len(matrix) - 1:
        for current_row in range(r + 1, len(matrix)):
            down_score += 1
            if (matrix[current_row][c] >= current_height):
                break
    left_score = 0
    if c > 0:
        for current_col in reversed(range(0, c)):
            left_score += 1
            if (matrix[r][current_col] >= current_height):
                break

    right_score = 0
    if c < len(matrix) - 1:
        for current_col in range(c + 1, len(matrix)):
            right_score += 1
            if (matrix[r][current_col] >= current_height):
                break

    return left_score * right_score * up_score * down_score

with open('input') as file:
    trees_visible = 0
    matrix = []
    for line in file:
        matrix.append([int(x) for x in list(line.strip('\n'))])

    print(get_max_scenic_score(matrix))
