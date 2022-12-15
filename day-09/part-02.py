memo = {}
rope = [[0, 0] for i in range(0, 10)]

def memoize():
    memo[tuple(rope[len(rope) - 1])] = True

def recalculatePosition(i):
    head = rope[i - 1]
    tail = rope[i]
    if (abs(head[0] - tail[0]) > 1):
        tail[0] += 1 if head[0] > tail[0] else -1
        if (head[1] != tail[1]):
            tail[1] += 1 if head[1] > tail[1] else -1
    elif (abs(head[1] - tail[1]) > 1):
        tail[1] += 1 if head[1] > tail[1] else -1
        if (head[0] != tail[0]):
            tail[0] += 1 if head[0] > tail[0] else -1

with open('input') as file:
    for line in file:
        dir, count = line.strip('\n').split(' ')
        for i in range(0, int(count)):
            if dir == 'R':
                rope[0][1] += 1
            if dir == 'L':
                rope[0][1] -= 1
            if dir == 'U':
                rope[0][0] += 1
            if dir == 'D':
                rope[0][0] -= 1

            for j in range(1, len(rope)):
                recalculatePosition(j)

            memoize()

    print(len(memo))
