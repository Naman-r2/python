def lastOccurence(l,k):
    if len(l) ==0:
        return -1
    n=len(l)-1
    if l[n]==k:
        return n
    return lastOccurence(l[:-1],k)
    


print(lastOccurence([1,2,3,2,2],3))