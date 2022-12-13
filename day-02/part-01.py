shape_score_dict = {'X': 1, 'Y': 2, 'Z': 3}
outcome_score_dict = {
    ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
    ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
    ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
}

with open('input') as file:
    score = 0

    for line in file:
        opponent_move, my_move = line.strip('\n').split(' ')
        score = score + shape_score_dict[my_move]
        score = score + outcome_score_dict[opponent_move, my_move]

    print(f'score: {score}')
