import json
from functools import cmp_to_key

def check_pair(signal_1, signal_2):
    if isinstance(signal_1, int) and isinstance(signal_2, int):
        if signal_1 == signal_2:
            return None

        return -1 if signal_1 < signal_2 else 1

    if isinstance(signal_1, list) and isinstance(signal_2, list):
        if len(signal_1) == 0 and len(signal_2) > 0:
            return -1
        elif len(signal_1) == 0 and len(signal_2) == 0:
            return None
        elif len(signal_2) == 0:
            return 1

        res = check_pair(signal_1[0], signal_2[0])
        if (res != None):
            return res

        return check_pair(signal_1[1:], signal_2[1:])

    if isinstance(signal_1, int) and isinstance(signal_2, list):
        return check_pair([signal_1], signal_2)

    if isinstance(signal_1, list) and isinstance(signal_2, int):
        return check_pair(signal_1, [signal_2])

    return 1

with open('input') as file:
    data = [json.loads(x.strip('\n')) for x in file if x != '\n'] + [[[2]]] + [[[6]]]
    data = sorted(data, key=cmp_to_key(check_pair))
    print(data.index([[2]]))
    print(data.index([[6]]))
    print((data.index([[2]]) + 1) * (data.index([[6]]) + 1))