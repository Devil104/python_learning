names=['i', 'love', 'you']
l=[]

for person in names:
    l.append(person)
print(l)
print([person for person in names])

l=[]
for person in names:
    l.append(person + ' baby.')
print(l)
print([person +' baby' for person in names])

markets={'corola': 9, 'bagun' :10, 'badhacopy' :3}
l=[]
for market in markets:
    if markets[market]<5:
        l.append(market)
print(l)
print([market for market in markets if markets[market]<5])
