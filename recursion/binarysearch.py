def binaryshelper(l,x,s,e):
    if s>e:
        return False
    m= s+(e-s)//2
    if l[m]==x:
        return True
    if l[m]<x:
        return binaryshelper(l,x,m+1,e) 
    
    return binaryshelper(l,x,s,m-1)
def binarys(l,x):
    return binaryshelper(l,x,0,len(l))

print(binarys([1,3,4,8,9,10],8))