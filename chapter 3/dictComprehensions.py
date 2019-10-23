# list of tuples
DIAL_CODES=[
    (21,'TEH'),
    (13,'ESF')
]

# key:value
city_code = {city:code for code,city in DIAL_CODES}
print(city_code)
# {'TEH': 21, 'ESF': 13}


res = {code:city for city,code in city_code.items() if code>15}
print(res)
# {21: 'TEH'}
