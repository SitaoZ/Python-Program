from collections import Counter
counter = Counter({'A': 10, 'C': 5, 'H': 7})
counter.most_common()
# [('A', 10), ('H', 7), ('C', 5)]
sorted(counter.items())
# [('A', 10), ('C', 5), ('H', 7)]
