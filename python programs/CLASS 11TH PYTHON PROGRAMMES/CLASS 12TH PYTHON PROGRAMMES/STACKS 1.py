a=[]
b='Y'
while b.upper()=='Y':
    d={}
    i=input('Enter book id:')
    n=input('Enter name of the book:')
    p=float(input('Enter price:'))
    d['Book Id']=i
    d['NAME']=n
    d['PRICE (in RS)']=p
    a.append(d)
    b=input('Do you want to enter more data? Y/N')
print('DATA ENTERED')
e=input('DO YOU WANT SEE THE DATA? Y/N')
if e.upper()=='Y':
    for q in a:
        print(q)
