l=eval(input('Enter a list of numbers:'))
ln=len(l)
for a in range(ln):
      for b in range(ln-1-a):
            if l[b]>l[b+1]:
                  l[b],l[b+1]=l[b+1],l[b]
      print('List after pass',a+1,'is',l)
print('Updated list is:',l)
            
