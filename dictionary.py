#dictionary={'black':2, 'bluse':5}
#print(dictionary.get('blue'))

#contact={'rony':{'phone: 015-34830574', 'email: rajibdave00@gmail.com'},'angcon':{'phone :013-234675', 'email: tahbixbx@gmail.com'}}
#print(contact['rony'])

sentence='hey baby how r y?'
l={
    'hey':1,
    'how':3
    }
l.update({'hey':2})
print(l)
print(list(l.items()))
print(l.keys())
print(l.values())
print(l)
l['baby']=4
print(l)
print(l.popitem())
print(l)
l.clear()
print(l)
