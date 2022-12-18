from collections import defaultdict, Counter

def is_anagram(a, b):
    characters = defaultdict(lambda: 0)
    for i in a:
        characters[i] += 1
    for i in b:
        characters[i] -= 1
    return len([key for (key, value) in characters.items() if value != 0]) == 0

# cool
def is_anagram_counter(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    return counter_a == counter_b

print(is_anagram('abc', 'cba'))
print(is_anagram_counter('abc', 'cba'))
