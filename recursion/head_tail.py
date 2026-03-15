#head recursion
def Hfact(n):
    if n==0:
        return 1
    smallAnswer=Hfact(n-1)
    finalAnswer =n*smallAnswer
    return finalAnswer

#tail recursion (no calculation after recursion call)

def Tfact(n,accumulator=1):
    if n==0:
        return accumulator
    accumulator=accumulator*n
    return Tfact(n-1,accumulator)

print(Hfact(4),Tfact(4))