l = ['yeganeh', 'salami', '1994', '09', '08']
print(l[:2])
# ['yeganeh', 'salami']
print(l[2:])
# ['1994', '09', '08']
print(l[-2:])
# ['09', '08']
print(l[::-1])
# ['08', '09', '1994', 'salami', 'yeganeh']
print(l[::-2])
# ['08', '1994', 'yeganeh']

l[0::4] = range(2)
print(l)
# [0, 'salami', '1994', '09', 1]

t=('yeganeh', 'salami',['1994', '09', '08'])
# t[2]+=['20','15']
print(t)