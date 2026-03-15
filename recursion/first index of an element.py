def firstOccurence(l1,k):
    if len(l1)==0:
        return -1
    if l1[0]==k:
        return 0 
    ans =  firstOccurence(l1[1:],k) 
    if ans == -1:
        return ans 
    else:
        return ans+1

    

print(firstOccurence([3,2,5,2,8,2,1],2))
#better approach
def firstOccurenceBetter(l1,k,index):
    if len(l1)== index:
        return -1
    if l1[index]==k:
        return index
    return firstOccurenceBetter(l1,k,index+1) 
    

    

print(firstOccurenceBetter([3,2,5,2,8,2,1],2,0))