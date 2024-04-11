#dict = { key :value}


data = {
        "id":[1,2,3,4],
        "name":["user1","user2","user3","user4"],
        "password":[111,222,333,444]
}

pos = -1
for i in data:
   
    if(i=="name"):
        n = data[i]
        name = input("enter name")
        print(n)
        for user in  n:
            if name ==user:
                pos = n.index(name)
                break
    print(pos)
    if i =="password":
        p = data[i]
        password = int(input("enter password"))
        print(p)
        print(pos)
        if password ==p[pos]:
            print("user login")
            break

""" print(data)

name = input("enter name")
if(name in data['name']):
    print("login")

else:
    print("not login")

 """""" data = {"id":1,"name":"user","age":30,"salary":400} """


""" data.pop("salary")
print(data)
 """
""" data['dpt'] = "acc"

print(data)
data.update({"dob":"1990/2/2"})

print(data)

del data["name"]

print(data) """

""" 
print(data)
print(data["name"])
for d in data:
    print(d)
 """

""" for d in data.values():
    print(d) """


""" for d in data.keys():
    print(d) """

""" 
for d in data.items():
    print(list(d)) """