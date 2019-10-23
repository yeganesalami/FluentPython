from types import MappingProxyType


dictionary = {'one': 1, 'two': 2}

dictionary_proxy = MappingProxyType(dictionary)

print(dictionary)
# {'one': 1, 'two': 2}
print(dictionary_proxy)
# {'one': 1, 'two': 2}

print(dictionary_proxy['one'])
# 1

dictionary_proxy['one'] = 'yeganeh'
# TypeError : 'mappingproxy' object does not support item assignment