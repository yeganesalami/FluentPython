import collections
import random

pylookup = collections.ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4},vars(random))
print(pylookup)
#  ChainMap groups multiple dicts together


ct = collections.Counter('yeganehh')
print(ct)
# Counter({'e': 2, 'h': 2, 'y': 1, 'g': 1, 'a': 1, 'n': 1})

print(ct.most_common(4))
# [('e', 2), ('h', 2), ('y', 1), ('g', 1)]