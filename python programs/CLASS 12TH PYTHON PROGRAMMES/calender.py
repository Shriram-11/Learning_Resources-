m=int(input('ENTER MONTH:'))
y=int(input('ENTER YEAR:'))
mm={1:'JANUARY',2:'FEBRUARY',3:'MARCH',4:'APRIL',5:'MAY',
    6:'JUNE',7:'JULY',8:'AUGUST',9:'SEPTEMBER',10:'OCTOBER',
    11:'NOVEMBER',12:'DECEMBER'}

d=(y-1)%400
d=(d//100)*5 + ((d%100) - (d%100)//4) + ((d%100)//4)*2
d=d%7
nly=[31,28,31,30,31,30,
     31,31,30,31,30,31]
ly=[31,29,31,30,31,30,
     31,31,30,31,30,31]
s=0
if y%4==0:
    for i in range(m-1):
        s+=ly[i]
else:
    for i in range(m-1):
        s+=nly[i]

d+=s%7
d=d%7

space=' '
space=space.rjust(2,' ')

print(mm[m],y)
