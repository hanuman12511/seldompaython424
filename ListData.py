#List === []

data = [3,4,8,4,4]
print(data)

del data

print(data)
""" data.reverse()
print(data) """
""" data.sort()
print(data) """

""" data.extend([8,0])
print(data) """

""" pos = int(input("enter pos"))
item = int(input("enter item"))
data.insert(pos,item)

print(data) """

""" data.remove(4)
print(data) """

""" 
item = data.pop()
print(item)
print(data) """
""" n = int(input("enter number"))
data.append(n)
print(data)

n = int(input("enter number"))
data.append(n)
print(data)
 """
""" 
print(data)
n = len(data)
for i in range(n//2):
    data[i],data[n-i-1]=data[n-i-1] ,data[i] """

""" print(data) """

""" print(data)

data[0] ,data[-1] = data[-1],data[0]

print(data)
 """
""" print(data)
n = len(data)
for i in range(n//2):
    temp = data[i]
    data[i]  =data[n-i-1]
    data[n-i-1] = temp


print(data) """
""" n1 =9
n2 =8
print(n1,n2)
n1,n2 = n2,n1
print(n1,n2) """


#print(data)
""" max= data[0]
for i in data:
    if max <i:
        max = i

print(max)

 """
""" 
print(max(data))
print(min(data))
print(sum(data))
print(len(data)) """



""" sum = 0
for i in data:
    sum+=i
print(sum) """
""" 
ocount = 0
ecount=0

osum = 0
esum=0

even=[]
odd=[]
for i in data:
    if i%2==0:
        esum+=i
        even.append(i)
        ecount+=1
    else:
        osum+=i
        ocount+=1
        odd.append(i)


print("odd count=",ocount)
print("even count  =",ecount)

print("odd number sum=",osum)
print("even number sum=",esum)
print(even)
print(odd)

 """





""" 
      -2-1
[3,4,5,6,7]
 0 1 2 3 4 """

""" print(data[0])
print(data[-1]) """


""" for i in data:
    print(i) """

""" n = len(data) """
""" print(n) """


""" for i in range(n):
    print(data[i]) """