#to check whether a no. is greater than
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b>c or a>c>b:
    print('a is greatest ')
elif b>a>c or b>c>a:
        print('c is greatest')
elif c>a>b or c>b>a:
    print('c is greatEST')
elif a>=b>=c :
    print('all are equal') 
print('end of program')
