def merge(l,s,m,e):
    i=s
    j=m+1
    ans=[]

    while i<=m and j<=e:
        if l[i]<l[j]:
            ans.append(l[i])
            i+=1
        elif l[i]>l[j]:
            ans.append(l[j])
            j+=1
        elif(l[i]==l[j]):
            ans.append(l[i])
            ans.append(l[j])
            i+=1
            j+=1

    while i<=m:
        ans.append(l[i])
        i+=1

    while j<=e:
        ans.append(l[j])
        j+=1

    startOfMyAns=0
    startOfMyList=s
    while startOfMyList<=e:
        l[startOfMyList] = ans[startOfMyAns]
        startOfMyAns+=1
        startOfMyList+=1

    return




def mergesort(l,s,e):
    if s>=e:
        return
    m=s+(e-s)//2
    mergesort(l,s,m)
    mergesort(l,m+1,e)

    merge(l,s,m,e)
    return

    
    
l=[1,3,4,5,2]
mergesort(l,0,len(l)-1)
print(l)