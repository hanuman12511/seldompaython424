""" n1 = 9
n2= 8
add = n1+n2
sub = n1-n2
print(add)
print(sub) """

# default

""" def Add():
    n1 = 7
    n2 =8
    r= n1+n2
    print(r)




def Sub():
    n1 = 7
    n2 =8
    r= n1-n2
    print(r)

while (True):
        n = int(input("enter 1 for sub and 2 for add 3 for break"))

        if(n==1):
            Sub()
        elif (n==2):
            Add()
        elif (n==3):
             break
        else:
            print("not use") """


def Add(n1,n2):
    r= n1+n2
    print(r)




def Sub(n1,n2):
    r= n1-n2
    print(r)

while (True):
   
        n = int(input("enter 1 for sub and 2 for add 3 for break"))
    
        if(n==1):
            n1 = int(input("enternumver"))
            n2 = int(input("enternumver"))
            Sub(n1,n2)
        elif (n==2):
            n1 = int(input("enternumver"))
            n2 = int(input("enternumver"))
            Add(1,n2)
        elif (n==3):
             break
        else:
            print("not use")