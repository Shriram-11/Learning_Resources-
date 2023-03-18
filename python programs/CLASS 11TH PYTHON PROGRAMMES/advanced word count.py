a=input('Enter a string:')
sp=alp=dig=spc=0
for b in a:
    if b==' ':
        sp+=1
    elif b.isdigit():
        dig+=1
    elif b.isalpha():
        alp+=1
    else:
        spc+=1
c=a.split()
wrd=len(c)
tot=alp+dig+spc
print('No. of spaces:',sp)
print('No. of alphabets:',alp)
print('No. of digits:',dig)
print('No. of special character:',spc)
print('Total words:',wrd)
print('Total no. of special characters:',tot)
