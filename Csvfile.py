import csv
"""
id    ,  name  ,  age
1     ,  "user" ,   40
2    ,   "user1",  43
"""

""" with open("filedata.csv","w") as file:
    writedate = csv.writer(file)
    writedate.writerow(["id","name","age"]);
    writedate.writerow([1,"user",30]);
    writedate.writerow([2,"user1",34]);
    writedate.writerow([3,"user3",45]);
    writedate.writerow([4,"user4",47]);
    writedate.writerow([5,"user5",23]);


with open("filedata.csv","r") as file:
    readerdata = csv.reader(file)
    for row in readerdata:
        print(row)

 """
data = {id:[1,2,3,4],"name":["user1","user2","user3","user4"]}
with open("dictdata.csv","w") as file:
    writedict = csv.DictWriter(file,["id","name"])
    writedict.writerows([{"id":1,"name":"user1"},{"id":2,"name":"user2"}])


with open("dictdata.csv","r") as file:
    readerdict = csv.DictReader(file)
    for row in readerdict:
        print(row)
  