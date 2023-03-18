#program to read a string and find the required value frm it
a=eval(input('Enter a string or list:'))
b=eval(input('Enter value to search:'))
ndx=-1
for c in range(len(a)):
    if b==a[c]:
        ndx=c
        break
if ndx!=-1:
    print(b,'found at index',ndx)
else:
    print('NOT FOUND!!!')
    
        
