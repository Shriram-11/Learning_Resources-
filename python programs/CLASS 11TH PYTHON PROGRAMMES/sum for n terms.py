count=0
tot=0
n=int(input('enter number of terms up to which you want the sum:'))
for a in range(1,n+1):
    count+=a
print('the sum up to',n,'terms is',count)
