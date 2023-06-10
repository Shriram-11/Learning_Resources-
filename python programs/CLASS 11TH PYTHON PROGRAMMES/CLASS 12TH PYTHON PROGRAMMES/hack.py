import sys

sum = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(n):
        if (n % 3 == 0 or n % 5 == 0):
            print(i)
            sum += i
    print(sum)
    sum = 0
