#sum of digits
def DigitsSum(n):
    if n==0:
        return 0
    p=int(n/10)
    r=int(n%10)
    return r + DigitsSum(p)

print(DigitsSum(456))
