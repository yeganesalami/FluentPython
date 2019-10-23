colors=['red','green','yellow']
sizes=['s','m','l']

products = [(color,size) for color in colors for size in sizes]
print(products)
#[('red', 's'), ('red', 'm'), ('red', 'l'), ('green', 's'), ('green', 'm'), ('green', 'l'), ('yellow', 's'), ('yellow', 'm'), ('yellow', 'l')]

##############################################################################################################################################

for tshirt in('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)
# red s
# red l
# red m
# green s
# green m
# green l
# yellow s
# yellow m
# yellow l