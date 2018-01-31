from collections import defaultdict

paris = [('a', 1), ('a', 2), ('a', 3), ('b', 4), ('b', 5)]

d = defaultdict(list)
for key, value in paris:
    d[key].append(value)
