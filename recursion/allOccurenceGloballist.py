#in a global list
l1=[]
def indexg(l,x,i):
    if len(l)==i:
        return 
    if l[i]==x:
        l1.append(i)
    indexg(l,x,i+1)


indexg([3,2,5,2,8,2,1],2,0,) #starting index

print(l1)

#as a new list


def index(l,x,i):
    if len(l)==i:
        return []
    k=index(l,x,i+1)   
    if l[i]==x:
        k.insert(0,i)
        return  k
    else:
        return k
    
     
    


print(index([3,2,5,2,8,2,1],2,0,)) #starting index

