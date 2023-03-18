#fibonacci series
n=int(input('Enter number of terms:'))
a=0
b=1
print(a)
print(b)
for d in range(1,n-1):
    c=a+b
    print(c)
    a,b=b,c
