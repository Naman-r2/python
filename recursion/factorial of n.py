#factorial of n
def fact(n):
    if n<0:
        print("invalid input")
        return 
    if n==1 or n==0:#base case
        return 1
    return n*fact(n-1)

print(fact(5))