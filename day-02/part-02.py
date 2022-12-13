outcome_score_dict = {'X': 0, 'Y': 3, 'Z': 6}
shape_score_dict = {
    ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
    ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
    ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
}

with open('input') as file:
    score = 0

    for line in file:
        opponent_move, my_move = line.strip('\n').split(' ')
        score = score + outcome_score_dict[my_move]
        score = score + shape_score_dict[opponent_move, my_move]

    print(f'score: {score}')
