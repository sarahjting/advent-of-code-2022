memo = {}
tail = [0, 0]
head = [0, 0]

def memoize():
    memo[tuple(tail)] = True

with open('input') as file:
    for line in file:
        dir, count = line.strip('\n').split(' ')
        for i in range(0, int(count)):
            if dir == 'R':
                head[1] += 1
            if dir == 'L':
                head[1] -= 1
            if dir == 'U':
                head[0] += 1
            if dir == 'D':
                head[0] -= 1

            if (abs(head[0] - tail[0]) > 1):
                tail[0] += 1 if head[0] > tail[0] else -1
                if (head[1] != tail[1]):
                    tail[1] += 1 if head[1] > tail[1] else -1
            elif (abs(head[1] - tail[1]) > 1):
                tail[1] += 1 if head[1] > tail[1] else -1
                if (head[0] != tail[0]):
                    tail[0] += 1 if head[0] > tail[0] else -1

            memoize()

    print(len(memo))
