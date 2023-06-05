# RECURSION-FIBONACCI
'''def fib(a):
    if a<=1:
        return a
    return fib(a-1)+fib(a-2)

a=int(input('Enter no. of terms you want on fibonnaci series:'))
print('FIBONACCI SERIES')
if a<=0:
    print('INVALID INPUT!!!')
else:
    for b in range(a):
        print(fib(b),end=',')
'''
import sys
i = a = s = 0


def fib(a):
    if a <= 1:
        return a
    return fib(a-1)+fib(a-2)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = fib(i)
    while (a <= n):
        if (a % 2 == 0):
            s += a
        i = i+1
        a = fib(i)
    print(s)
    s = 0/
