def calculate_cycles(lines):
    cycles = [1]
    current_cycle = 0

    def current_cycle_value():
        return cycles[current_cycle]

    def noop():
        nonlocal current_cycle
        cycles.append(current_cycle_value())
        current_cycle += 1

    def addx(delta):
        nonlocal current_cycle
        cycles.append(current_cycle_value())
        cycles.append(current_cycle_value() + delta)
        current_cycle += 2

    for line in lines:
        if (line[0:4] == 'noop'):
            noop()
        else:
            operation, delta = line.strip('\n').split(' ')
            addx(int(delta))

    return cycles

with open('input') as file:
    cycles = calculate_cycles([x for x in file])
    for row in range(0, 6):
        string = ''
        for col in range(0, 40):
            cycle_value = cycles[row * 40 + col]
            string += '#' if (abs(cycle_value - col) < 2) else '.'
        print(string)
