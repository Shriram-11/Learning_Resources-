#program to find longest and shortest from a list of string
a=(input('Enter a string:'))
mn=len(a[0])
mx=len(a[0])
maxw=minw=a[0]
c=len(a)
for b in range(1,c):
    if len(a[b])>mx:
        maxw=a[b]
        mx=len(a[b])
    elif len(a[b])<mn:
        minw=a[b]
        mn=len(a[b])
print('the longest word is :',maxw,' lenght=',mx)
print('the shotest word is :',minw,' lenght=',mn)
