def Fact1(n):
    if(n>0):
        if n==0:
            return 1
        return n*Fact1(n-1)
    return 1