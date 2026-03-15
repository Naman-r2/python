def ls(l,n,i=0):
    if len(l)==i:
        return -1
    if l[i]== n:
        return i
    return ls(l,n,i+1)

print(ls([1,2,3],2))
        
    