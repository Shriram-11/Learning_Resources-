#program to calculate sum to n terms
n=int(input('enter a number of your choice'))
for a in range(1,n+1):
    tot=0
    tot+=a
    to=n+tot
    print('the sum upto ',n,'terms is:',to)
