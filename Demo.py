""" print("hello")

n1 = 8  #   A-Z   a-z  0-9  _

print(n1)

n1 = input("enter number")

print(n1) """


""" n1 = input("enter n1") # return string
n2 = input("enter n2")

print(n1,n2)
r=int(n1)+ int(n2)
print(r)
 """
# 8=5+3

""" n1 = input("enter n1") # return string
n2 = input("enter n2")
r=int(n1)+ int(n2)
print(r,"=",n1,"+",n2)
 """
# + - * / // % **

""" n1 = input("enter n1") # return string
n2 = input("enter n2")
r=int(n1)- int(n2)
print(r)
r=int(n1)* int(n2)
print(r)
r=int(n1)/ int(n2)
print(r)
r=int(n1)// int(n2)
print(r)
r=int(n1)% int(n2)
print(r)
r=int(n1)** int(n2)
print(r) """


#+=  -=   *=   /=   **=  //=

""" 
n1 = 5
print(n1) """
""" n1= n1+2 """
""" n1+=
print(n1) """

# > < >= <= != == bool true false

""" n1 =7
n2 =5
r= n1<n2  # 7<5 false
print(r)
r= n1>=n2  # 7> 5 true
print(r)
r= n1<=n2  #7<=5  false
print(r)
r= n1!=n2  # 7!=5 true
print(r)
r= n1==n2  # 7==5 false
print(r)
 """

#and or not  true false 

#true and true = true
#false or ture = false
#not(false) = true

""" 
n1= 5
n2 =6
r= n1 < 10 and n2 <30
print(r) """

""" n1= 5
n2 =6
r= n1 >10 or n2 >30
print(r)
 """

""" n1 = 6
n2 =7
r = not(n1>n2) # not(6>7 false) true
print(r)
 """


# control statement 
# if
# if else
# if elif.... else


""" if True:
    print("if run") """


""" if False:
    print("if run")

else:
    print("else run") """

""" 
if False:
    print("if run")
elif True:
    print("elif run")
else:
    print("else run") """


""" 
if False:
    print("if run")
elif False:
    print("elif run")
else:
    print("else run") """


""" n1 = -9
if n1>0:
    print("+")
else:
    print("-") """


""" n1 = 7

if n1%2==0:
    print("even")
else:
    print("odd") """

# max find
""" n1 = 5
n2 = 93
if(n1>n2):
    print(n1)
else:
    print(n2) """


""" n1 = 44
n2 = 5
if(n1<n2):
    print(n1)
else:
    print(n2) """


""" n1 = 7
n2 = 35
n3 = 44
if (n1>n2 and n1>n3):
    print(n1)
elif n2>n3:
    print(n2)
else:
    print(n3) """

""" n1 = 7
n2 = 65
n3 = 4
if(n1>n2):
    if n1>n3:
        print(n1) 
    else:
        print(n3)
elif n2>n3:
    print(n2)#65
else:
    print(n3) """


#loop
# 1 2 3 4 5 6
""" 
start =i = 1
end i<=6
i=i+1 
 """


#while
""" 
start 
while(end):
    print 
    i+=1 """



""" i=1
while(i<=10):
    print(i,end="\t")
    i+=1 """

""" t =2
i=1
while(i<=10):
    print(i*t,end="\t")
    i+=1 """

""" sum =0
i=1
while(i<=10):
    sum=sum+i
    i+=1

print(sum) """


""" sum =0
i=1
while(i<=10):
    if(i%2==0):
        sum=sum+i
    i+=1

print(sum) """

""" sum =0
i=1
while(i<=10):
    if(i%2==1):
        sum=sum+i
    i+=1

print(sum) """