from collections import deque
from math import floor
from functools import reduce

class Monkey:
    def __init__(self, input):
        self.inspections_count = 0

        self.items = deque([int(x) for x in input[1].replace(',', '').split(':')[1].strip(' ').split(' ')])

        operation_line = input[2].split(' ')
        self.operator_constant = operation_line.pop()
        self.operator_operator = operation_line.pop()

        self.test_divisor = int(input[3].split(' ').pop())
        self.true_monkey = int(input[4].split(' ').pop())
        self.false_monkey = int(input[5].split(' ').pop())

    def __repr__(self):
        return {
            'inspections_count': self.inspections_count,
            'items': self.items
        }.__repr__()

    def test_item(self, item):
        return item % self.test_divisor == 0

    def operate_on_item(self, item):
        if self.operator_constant.isnumeric():
            if self.operator_operator == '*':
                return item * int(self.operator_constant)
            elif self.operator_operator == '+':
                return item + int(self.operator_constant)
        else:
            if self.operator_operator == '*':
                return item * item

        print('unrecognised operator')


def readFile(data):
    monkeys = []
    monkeys_number = int((len(data) + 1)/7)
    for i in range(0, monkeys_number):
        monkeys.append(Monkey(data[i * 7:(i * 7 + 6)]))

    return monkeys

def executeRound(monkeys):
    divisor = reduce(lambda a, b: a*b, [monkey.test_divisor for monkey in monkeys])
    for monkey in monkeys:
        while (monkey.items):
            inspecting_item = monkey.items.popleft()
            inspecting_item = monkey.operate_on_item(inspecting_item)
            inspecting_item %= divisor
            monkey.inspections_count += 1
            monkeys[monkey.true_monkey if monkey.test_item(inspecting_item) else monkey.false_monkey].items.append(inspecting_item)

    return monkeys


with open('input') as file:
    monkeys = readFile([x.strip('\n') for x in file])

    for i in range(0, 10000):
        monkeys = executeRound(monkeys)

    inspection_scores = sorted([monkey.inspections_count for monkey in monkeys], reverse = True)
    print (inspection_scores)
    print(inspection_scores[0] * inspection_scores[1])
