#find no. of vowels,consonants,uppercase,lowercase characters
a=input('Enter text:')
def charcount(a):
    vcnt=ccnt=ucnt=lcnt=sp=0
    for b in range(len(a)):
        if a[b] in 'aeiou' or a[b] in 'AEIOU':
            vcnt+=1
        elif a[b] in 'bcdfghjklmnpqrstvwxyz' or a[b] in 'BCDFGHJKLMPQRSTVWXY':
            ccnt+=1
        else:
            sp+=1
    for c in range(len(a)):
        if a[c].isupper():
            ucnt+=1
        else:
            lcnt+=1
    tot=lcnt+ucnt+sp
    print('No. of lowercase characters:',lcnt)
    print('No. of uppercase characters:',ucnt)
    print('No. of vowels:',vcnt)
    print('No. of consonants:',ccnt)
    print('Total no. of characters:',tot)
    print('No. of special characters:',sp)

print(charcount(a))



