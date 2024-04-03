""" n =12356
sum=0
while(n!=0):
    r = n%10
    sum+=r
    print(r)
    n//=10
print("******************")
print(sum) """

""" n =12356
print(n)
sum=0
while(n!=0):
    r = n%10
    if(r%2==0):
        sum+=r
        print(r)
    n//=10
print("******************")
print(sum) """

""" n =12356
print(n)
sum=0
while(n!=0):
    r = n%10
    if(r%2==1):
        sum+=r
        print(r)
    n//=10
print("******************")
print(sum) """


""" n =12356897
print(n)
count=0
while(n!=0):
    count +=1
    n//=10
print("******************")
print(count) """


""" n =12356
print(n)
n1 =0
n2=0
while(n!=0):
    r = n%10
    if(r%2==0):
        n1=n1*10+r
        print(r)
    else:
        n2=n2*10+r
    n//=10
print("******************")
print("even digit",n1)
print("odd digit",n2) """

#12=10+2=>1*10+2

n1 =8976
print(n1)
sum=0
n2=0
n3=0
while n1!=0:
    r = n1%10
    if r%2==0:
        n2=n2*10+r
    else:
        n3=n3*10+r
    n1 //=10


print("**********")
print("even digit",n2)
print("odd digit",n3)