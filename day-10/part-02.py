class Cycles:
    def __init__(self, input):
        self.cycles = [1]
        self.current_cycle = 0

        for line in input:
            if (line[0:4] == 'noop'):
                self.noop()
            else:
                operation, delta = line.strip('\n').split(' ')
                self.addx(int(delta))

    def current_value(self):
        return self.cycles[self.current_cycle]

    def noop(self):
        self.cycles.append(self.current_value())
        self.current_cycle += 1

    def addx(self, delta):
        self.cycles.append(self.current_value())
        self.cycles.append(self.current_value() + delta)
        self.current_cycle += 2

with open('input') as file:
    cycles = Cycles([x for x in file]).cycles
    for row in range(0, 6):
        string = ''
        for col in range(0, 40):
            cycle_value = cycles[row * 40 + col]
            string += '#' if (abs(cycle_value - col) < 2) else '.'
        print(string)
