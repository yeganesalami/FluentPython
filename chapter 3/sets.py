a = ['spam', 'spam', 'yeganeh', 'yeganeh', 'salami']
b = ['salami', 'salami', 'spam']

a_set = set(a)
b_set = set(b)

print(list(a_set))
# ['yeganeh', 'spam', 'salami']
print(a_set)
# {'spam', 'salami', 'yeganeh'}
print(b_set)
# {'spam', 'salami', 'yeganeh'}


print(len(a_set & b_set))  # 2
# as same as
# found = 0
# for n in a_set:
#     if a in b_set"
#     found += 1

print(len(a_set - b_set))  # 1
print(len(a_set | b_set))  # 3


traverler_id = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
d1 = dict(traverler_id)

print('d1:', d1.keys())
# d1: dict_keys(['USA', 'BRA', 'ESP'])
print('d1:', d1.values())
# d1: dict_values(['31195855', 'CE342567', 'XDA205856'])
print(sorted(traverler_id, key=lambda x: x[0]))
# sort by x[0] 
# [('BRA', 'CE342567'), ('ESP', 'XDA205856'), ('USA', '31195855')]