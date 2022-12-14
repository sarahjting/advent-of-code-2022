from collections import deque

def parseInput(file):
    raw = []
    for line in file:
        if (line == '\n'):
            break
        else:
            raw.append(line)

    stackLegend = [x for x in raw.pop().strip('\n').split(' ') if x != '']
    numStacks = int(stackLegend[len(stackLegend) - 1])
    stacks = {key: deque() for key in range(1, numStacks + 1)}

    for line in raw:
        for stackIndex in range(1, numStacks + 1):
            crateSymbol = line[(stackIndex - 1) * 4 + 1]
            if crateSymbol != ' ':
                stacks[stackIndex].append(crateSymbol)

    return stacks

with open('input') as file:
    stacks = parseInput(file)

    do_skip = True
    for line in file:
        numCrates, srcStack, dstStack = [int(x) for x in line.strip('\n').split(' ') if x.isdigit()]
        appendable = deque()
        for i in range(0, numCrates):
            appendable.appendleft(stacks[srcStack].popleft())
        stacks[dstStack].extendleft(appendable)

    print(''.join([d[0] for (key, d) in stacks.items()]))
