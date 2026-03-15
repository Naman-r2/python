#2^n
def power2(n):
    if n==1 :
        return 2
    return 2*power2(n-1)

print(power2(5))