
data = {
    "id":[100,200,300,400],
    "name":["user1","user2","user3","user4"],
    "password":[111,222,333,444]
}

print(data)
listkey = []
for d in data:
    listkey.append(d)
print(listkey)


name = "user2"

for i in listkey:
    if name in data.get(i):
        print(data.get(i))



""" data = {"id":100,"name":"user","salary":5000} """
""" print(data)
key =input("enter key")
value =input("enter value")

data.update({key:value})

print(data) """
""" 
key =input("enter key")
value =input("enter value")

data[key] = value
print(data) """

""" del data["name"]

print(data) """

""" data.pop("name")
print (data) """
""" data.popitem()
print(data) """

""" 
data1 = data.get("name")
print(data1) """

""" data.clear()
print(data) """



""" 
data1 =data.copy()
print(data1)
 """

""" print(len(data))
 """