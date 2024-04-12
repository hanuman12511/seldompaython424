w = open("w.txt","w")
w.write("hanu")
w.close()


r= open("w.txt","r")

for i in r:
    print(i)