import json


with open('C:/Users/ASUS/Desktop/New folder/pic.txt') as json_data: 
     p=json.load(json_data)

list=p['data']
for person in list['movies']:
    print(person['title'])
    print(person['year'])
    print(person["title_long"])


