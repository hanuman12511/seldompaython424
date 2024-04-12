#createfile  = open("filename","mode") #  r ,w , a

def CreateFile():
    filename = input("enter file name")
    createfile = open(filename,"w")
    name = input("enter name")
    createfile.write(name)
    age = input("enter age")
    createfile.write(age)
    classname = input("enter class")
    createfile.write(classname)
    
    createfile.write("\n")
def ReadFile():
    filename= input("enter filename")
    readdata = open(filename,"r") 

    for data in readdata:
        print(data)
    
def appendData():
    filename = input("enter filename")
    app= open(filename,"a")
    name = input("enter name")
    age = input("enter age")
    classname = input("enter class")
    app.write(name)
    app.write(age)
    app.write(classname)
    app.write("\n")
while True:
    ch = int(input("1 for write file\n2 for read file\n3 form append file\n4 for break control"))
    if ch ==1:
        CreateFile()
    elif ch ==2:
        print("read file")
        ReadFile()
    elif ch == 3:
        print("data append")
        appendData()
    elif ch == 4:
        break
    else:
        print("enter right value")