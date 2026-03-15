#power of number

def PoN(base,exp):
    if  exp==1:
        return base
    return base * PoN(base,exp-1)
    
print(PoN(2,5))