# functions in python are first class objects
# first class objects means:
# - created at runtime
# - assigned to a variable or element in a data structure
# - passed as an argument to a function
# - return as the result of a function

# int strigs and dicts are other example of first-class objects in python
# one the halmark of functional programming is the use of higher-order functions = a function taht takes a functions as argument or returns function as result

from operator import itemgetter

fruits = ['apple', 'banana', 'fig']


def reverse(word):
    return word[::-1]


print(sorted(fruits, key=reverse))
# ['banana', 'apple', 'fig']

# map and filter return generators

# 3

# In the example below the cities are printed sorted by contry code (field 1)
# itemgetter(1) == lambda fields : fileds[1]

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Dehli NCR', 'IN', 21.935, (35.689722, 139.691667)),
    ('Sao Paulo', 'BR', 19.935, (35.689722, 139.691667))
]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# ('Sao Paulo', 'BR', 19.935, (35.689722, 139.691667))
# ('Dehli NCR', 'IN', 21.935, (35.689722, 139.691667))
# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))


cc_name = itemgetter(0, 1)
for city in metro_data:
    print(cc_name(city))

# ('Tokyo', 'JP')
# ('Dehli NCR', 'IN')
# ('Sao Paulo', 'BR')
