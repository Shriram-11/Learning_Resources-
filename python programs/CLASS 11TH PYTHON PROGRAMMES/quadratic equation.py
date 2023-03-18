#to find roots of quadratic equations
import cmath
import math
print('I quadratic equation ax**2 + bx + c=0')
print('a!=0')
a=int(input('Value of a:'))
b=int(input('Value of b:'))
c=int(input('Value of c:'))
d=(b**2)-(4*a*c)
if d==0:
      print('ROOTS ARE REAL AND EQUAL')
      r1=-b/(2*a)
      r2=r1
elif d>0:
      print('ROOTS ARE REAL AND UNEQUAL')
      r1=(-b+ math.sqrt(d))/(2*a)
      r2=(-b - math.sqrt(d))/(2*a)
elif  d<0:
      print('ROOTS ARE COMPLEX')
      r1=(-b+ cmath.sqrt(d))/(2*a)
      r2=(-b - cmath.sqrt(d))/(2*a)
print('Roots of the given quadratic equation are:',r1,'and',r2)
      
