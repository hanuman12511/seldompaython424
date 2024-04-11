def Loop(n):
    
    if n==0:
        return 1
    
    return n*Loop(n-1)

print(Loop(5))



