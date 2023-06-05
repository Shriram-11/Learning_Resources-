import math
#factorial using recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input('Enter number of which you want to find factorial:'))
print('Factorial of',n,'is:',factorial(n))
print(math.factorial(n))
