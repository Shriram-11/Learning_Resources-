a=[]
b='Y'
d={}
while b.upper()=='Y':
    city=input('Enter name of the city:')
    pin=int(input('Enter pincode:'))
    d['CITY']=city
    d['PIN CODE']=pin
    print(d)
    a.append(d)
    b=input('Do you want to enter more data? Y/N')
print('DATA ENTERED')
print(a)
    
