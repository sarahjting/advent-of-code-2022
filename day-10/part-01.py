cycles = [1]
current_cycle = 0

def current_cycle_value():
    return cycles[current_cycle]

def noop():
    global current_cycle
    cycles.append(current_cycle_value())
    current_cycle += 1

def addx(delta):
    global current_cycle
    cycles.append(current_cycle_value())
    cycles.append(current_cycle_value() + delta)
    current_cycle += 2

with open('input') as file:
    for line in file:
        if (line[0:4] == 'noop'):
            noop()
        else:
            operation, delta = line.strip('\n').split(' ')
            addx(int(delta))

    print(sum([(key + 1) * value for (key, value) in enumerate(cycles) if key in (x - 1 for x in [20, 60, 100, 140, 180, 220])]))
