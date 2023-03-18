a=input('Enter a string:')
sp=char=0
for b in a:
    if b==' ':
        sp+=1
    else:
        char+=1
c=a.split()
wrd=len(c)
print('No. of spaces:',sp)
print('No of words :',wrd)
print('Total characters:',char)
