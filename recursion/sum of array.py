def sum(l):
    if  len(l)==0:
        return 0
    return l[0] + sum(l[1:])

print(sum([1,2,3,4,5]))


#tail
def sumT(l,accumulator=0):
    if len(l)==0:
        return accumulator
    
    accumulator += l[0]

    return sumT(l[1:],accumulator)

print(sumT([1,2,3]))
