def print1toN(n):
    if(n<=0):
        return
    
    print(n)
    print1toN(n-1)

print1toN(5)