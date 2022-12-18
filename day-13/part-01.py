import json

def check_pair(signal_1, signal_2):
    if isinstance(signal_1, int) and isinstance(signal_2, int):
        if signal_1 == signal_2:
            return None

        return signal_1 < signal_2

    if isinstance(signal_1, list) and isinstance(signal_2, list):
        if len(signal_1) == 0 and len(signal_2) > 0:
            return True
        elif len(signal_1) == 0 and len(signal_2) == 0:
            return None
        elif len(signal_2) == 0:
            return False

        res = check_pair(signal_1[0], signal_2[0])
        if (res != None):
            return res

        return check_pair(signal_1[1:], signal_2[1:])

    if isinstance(signal_1, int) and isinstance(signal_2, list):
        return check_pair([signal_1], signal_2)

    if isinstance(signal_1, list) and isinstance(signal_2, int):
        return check_pair(signal_1, [signal_2])

    return False

with open('input') as file:
    data = [x.strip('\n') for x in file]
    pairs_count = int((len(data) + 1)/3)
    pairs = [(json.loads(data[(x*3)]), json.loads(data[(x*3) + 1])) for x in range(0, pairs_count)]

    correct_pairs_count = 0
    for (key, (signal_1, signal_2)) in enumerate(pairs):
        if check_pair(signal_1, signal_2):
            correct_pairs_count += key + 1

    print(correct_pairs_count)