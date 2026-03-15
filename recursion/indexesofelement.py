def indexes(l,x,i):
    if len(l)==i:
        return
    if l[i]==x:
        print(i)
    indexes(l,x,i+1)
    



indexes([3,2,5,2,8,2,1],2,0)#starting index


#in a list
def indexel(l,x,i,l1):
    if len(l)==i:
        return 
    if l[i]==x:
        l1.append(i)
    indexel(l,x,i+1,l1)

l1 = []
indexel([3,2,5,2,8,2,1],2,0,l1) #starting index

print(l1)

