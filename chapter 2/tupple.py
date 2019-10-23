from collections import namedtuple

# tuple used as records
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traverler_id = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traverler_id):
    print('%s %s' % passport)

# BRA CE342567
# ESP XDA205856
# USA 31195855


for passport in ('%s %s' % p for p in sorted(traverler_id)):
    print(passport)

# BRA CE342567
# ESP XDA205856
# USA 31195855    


for country,_ in sorted(traverler_id):
    print(country)

# BRA
# ESP
# USA

User = namedtuple('User','name family birthDate location')
salami = User('yeganeh','salami',('1994','08','09'),('tehran','iran'))
print(salami)
# User(name='yeganeh', family='salami', birthDate=('1994', '08', '09'), location=('tehran', 'iran'))
print(salami.birthDate)
# ('1994', '08', '09')
print(salami[0])
# yeganeh
print(User._fields)
# ('name', 'family', 'birthDate', 'location')



print('###############################################################################')

User = namedtuple('User','name family birthDate location')
BirthDate = namedtuple('bd','year month day')
salami = User('yeganeh','salami',BirthDate('1994', '08', '09'),('tehran','iran'))
print(salami)
# User(name='yeganeh', family='salami', birthDate=bd(year='1994', month='08', day='09'), location=('tehran', 'iran'))
print(salami.birthDate.year)
# bd(year='1994', month='08', day='09')
s = User(*salami)
print(s)
# User(name='yeganeh', family='salami', birthDate=bd(year='1994', month='08', day='09'), location=('tehran', 'iran'))

for key,value in s._asdict().items():
    print(key+' : ',value)

# name :  yeganeh
# family :  salami
# birthDate :  bd(year='1994', month='08', day='09')
# location :  ('tehran', 'iran')


lax_coordinates=(33.9425, -118.408056)
latitude , longitude = lax_coordinates
print(latitude, longitude)