# map and filter return a map object whereas reduce return a single value
from functools import reduce
from operator import mul, itemgetter


def fact(n):
    return reduce(lambda a, b: a*b, range(1, 1+n))


print(fact(5))
##############################################################


def fact2(n):
    return reduce(mul, range(1, 1+n))


print(fact2(5))
##############################################################
