# partial functions in python allow one to derive a function with x parameter to a fucntion with
# fewer parameters and fixed values set for the more limited functions.
from functools import partial
from TagGenerator import tag


def multiply(x, y):
    return x*y


triple = partial(multiply, 2)
print(triple(4))  # 8
print(list(map(triple, range(1, 10))))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]


picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='a.jpg'))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]