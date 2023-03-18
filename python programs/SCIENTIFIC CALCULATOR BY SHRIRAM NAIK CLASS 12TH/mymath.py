#module created by me
import math
import cmath
def root(a,b):
    return a**(1/b)

def squarea(a):
    return a*a

def rectanglea(a,b):
    return a*b

def circlea(r):
    return 3.14*r*r

def squarep(a):
    return 4*a

def rectanglep(a,b):
    return 2*(a+b)

def circlec(r):
    return 2*3.14*r

def cubea(a):
    return 6*a*a

def cubev(a):
    return a*a*a

def cuboida(l,b,h):
    return 2*((l*b)+(b*h)+(h*l))

def cuboidv(l,b,h):
    return l*b*h

def cylindert(r,h):
    return 2*3.14*r*(h+r)

def cylinderc(r,h):
    return 2*3.14*r*h

def cylinderv(r,h):
    return 3.14*r*r*h

def conec(r,l):
    return 3.14*r*l

def conet(r,l):
    return 3.14*r*(l+r)

def conev(r,h):
    return (3.14*r*r*h)/3

def spheret(r):
    return 4*r*r*3.14

def spherev(r):
    return (4*3.14*r*r*r)/3

def hemispheret(r):
    return 3*3.14*r*r

def hemispherec(r):
    return 2*3.14*r*r

def hemispherev(r):
    return (2*3.14*r*r*r)/3

def frustumt(R,r,l):
    return (3.14*l*(R+r)+(3.14*(math.pow(R,2)+math.pow(r,2))))

def frustumc(R,r,l):
    return (3.14*l*(r+R))

def frustumv(R,r,h):
    return ((3.14*h*((R*R)+(r*r)+(r*R)))/3)

def slantheightf(R,r,h):
    return (((h*h)+((R-r)**2))**(1/2))

def slantheightc(r,h):
    return (((r*r)+(h*h))**(1/2))

def secter(a,r):
    return ((a*3.14*r*r)/360)

def arclenght(a,r):
    return((a*3.14*r)/180)

def rad(a):
    return ((a*3.14)/180)

def deg(r):
    return ((r*180)/3.14)

def vectorres(a,b,d):
    w=((a**2)+(b**2)+(2*a*b*math.cos(math.radians(d))))
    r=math.sqrt(w)
    return r

def vectordir(a,b,d):
    m=((b*math.sin(math.radians(d)))/(a+(b*math.cos(math.radians(d)))))
    return m

def vectoradd(a,b):
    t=[a[0]+b[0],a[1]+b[2],a[2]+b[2]]
    return t

def vectordot1(a,b):
    t=[a[0]*b[0],a[1]*b[1],a[2]*b[2]]
    return t

def vectordot2(x,y,d):
    a=x*y*math.cos(math.radians(d))
    return a

def vectorcross1(a,b):
    t=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    return t

def vectorcross2(x,y,d):
    a=x*y*math.sin(math.radians(d))
    return a

def lcm(a,b):
    if a>b:
        g=a
    else:
        g=b
    while(True):
        if g%a==0 and g%b==0:
            lcm=g
            break
        g+=1
    return lcm

def hcf(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if a%i==0 and b%i==0:
            hcf=i
        return hcf
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

def npr(n,r):
    return math.floor(fact(n)/fact(n-r))

def ncr(n,r):
    return (fact(n)/(fact(r)*fact(n-r)))

def mod(a,b):
    c=((a*a)+(b*b))
    r=math.sqrt(c)
    return r

def conjugate(a,b):
    b*=-1
    print(a,b,'i')

def lenghts(a,b,c):
    ans=0
    if a=='km':
        if b=='m':
            ans=c*1000
        elif b=='cm':
            ans=c*100000
        elif b=='mm':
            ans=c*1000000
        elif b=='nm':
            ans=10000000000000
        elif b=='mile':
            ans=c/1.609
        elif b=='yards':
            ans=c*1093.613
        elif b=='feets':
            ans=c*3280.84
        elif b=='inches':
            ans=c*39370.1
        elif b=='nautical miles':
            ans=c/1.852
    elif a=='m':
        if b=='km':
            ans=c/1000
        elif b=='cm':
            ans=c*100
        elif b=='mm':
            ans=c*1000
        elif b=='nm':
            ans=c*1000000000
        elif b=='miles':
            ans=c/1609
        elif b=='yards':
            ans=c*1.09361
        elif b=='feets':
            ans=c*3.281
        elif b=='inches':
            ans=c*39.37
        elif b=='nautical miles':
            ans=c/1852
    elif a=='cm':
        if b=='km':
            ans=c/100000
        elif b=='m':
            ans=c/100
        elif b=='mm':
            ans=c*100
        elif b=='nm':
            ans=c*10000000
        elif b=='miles':
            ans=c/169034
        elif b=='yards':
            ans=c/91.44
        elif b=='feets':
            ans=c/30.48
        elif b=='inches':
            ans=c/2.54
        elif b=='nautical miles':
            ans=c/185200
    elif a=='mm':
        if b=='km':
           ans=c/1000000
        elif b=='m':
           ans=c/1000
        elif b=='cm':
            ans=c/10
        elif b=='nm':
            ans=c*1000000
        elif b=='miles':
            ans=c*6.214/10000000
        elif b=='yards':
            ans=c/914
        elif b=='feets':
            ans=c/305
        elif b=='inches':
            ans=c/25.4
        elif b=='nautical miles':
            ans=c*5.4/10000000
    elif a=='nm':
        if b=='km':
            ans=c/1000000000000
        elif b=='m':
            ans=c/1000000000
        elif b=='cm':
            ans=c/10000000
        elif b=='mm':
            ans=c/1000000
        elif b=='miles':
            ans=c*6.214/10000000000000
        elif b=='yards':
            ans=c*1.094/1000000000
        elif b=='feets':
            ans=c/(3.048/100000000)
        elif b=='inches':
            ans=c*3.937/100000000
        elif b=='nautical miles':
            ans=c*5.4/10000000000000
    elif a=='miles':
        if b=='km':
            ans=c*1.609
        elif b=='m':
            ans=c*1609
        elif b=='cm':
            ans=c*160900
        elif b=='mm':
            ans=c*1609000
        elif b=='nm':
            ans=c*1609000000000
        elif b=='yards':
            ans=c*1760
        elif b=='feets':
            ans=c*5280
        elif b=='inches':
            ans=c*63360
        elif b=='nautical miles':
            ans=c/1.151

    elif a=='yards':
        if b=='km':
            ans=c/1094
        elif b=='m':
            ans=c/1.094
        elif b=='cm':
            ans=c*91.44
        elif b=='mm':
            ans=c*914.4
        elif b=='nm':
            ans=c*9144*100000
        elif b=='miles':
            ans=c/760
        elif b=='feets':
            ans=c*3
        elif b=='inches':
            ans=c*36
        elif b=='nautical miles':
            ans=c/2025
    elif a=='feets':
        if b=='km':
            ans=c/3281
        elif b=='m':
            ans=c/3.281
        elif b=='cm':
            ans=c*30.48
        elif b=='mm':
            ans=c*304.8
        elif b=='nm':
            ans=c*3048*100000
        elif b=='miles':
            ans=c/5280
        elif b=='yards':
            ans=c/3
        elif b=='inches':
            ans=c*12
        elif b=='nautical miles':
            ans=c/6076
    elif a=='inches':
        if b=='km':
           ans=c/39370
        elif b=='m':
            ans=c/39.37
        elif b=='cm':
            ans=c*2.54
        elif b=='mm':
            ans=c*25.4
        elif b=='nm':
            ans=c*254*100000
        elif b=='miles':
            ans=c/63360
        elif b=='yards':
            ans=c/36
        elif b=='feets':
            ans=c/12
        elif b=='nautical miles':
            ans=c/72913
    elif a=='nautical miles':
        if b=='km':
           ans=c*1.852
        elif b=='m':
            ans=c*1852
        elif b=='cm':
            ans=c*182500
        elif b=='mm':
            ans=c*1825000
        elif b=='nm':
            ans=c*1852000000000
        elif b=='miles':
            ans=c*1.151
        elif b=='yards':
            ans=c*2025
        elif b=='feets':
            ans=c*6076
        elif b=='inches':
            ans=c*72913
    return a,c,'='"{:.2e}".format(ans),b
def mass(a,b,c):
    ans=0
    if a=='tonne':
        if b=='kg':
            ans=c*1000
        elif b=='g':
            ans=c*1000000
        elif b=='quintal':
            ans=c*10
        elif b=='mg':
            ans=c*1000000000
        elif b=='pounds':
            ans=c*2204.62
    elif a=='quintal':
        if b=='tonne':
            ans=c/10
        elif b=='kg':
            ans=c*100
        elif b=='g':
            ans=c*100000
        elif b=='mg':
            ans=c*100000000
        elif b=='pounds':
            ans=c*220
    elif a=='kg':
        if b=='tonne':
            ans=c/1000
        elif b=='quintal':
            ans=c/100
        elif b=='g':
            ans=c*1000
        elif b=='mg':
            ans=c*1000000
        elif b=='pounds':
            ans=c*2.205
    elif a=='g':
        if b=='tonne':
            ans=c/1000000
        elif b=='quintal':
            ans=c/100000
        elif b=='kg':
            ans=c/1000
        elif b=='mg':
            ans=c*1000
        elif b=='pounds':
            ans=c/454
    elif a=='mg':
        if b=='tonne':
            ans=c/1000000000
        elif b=='quintal':
            ans=c/100000000
        elif b=='kg':
            ans=c/1000000
        elif b=='g':
            ans=c/1000
        elif b=='pounds':
            ans=c/453592
    elif a=='pounds':
        if b=='tonne':
            ans=c/2205
        elif b=='quintal':
            ans=c/220
        elif b=='kg':
            ans=c/2.205
        elif b=='g':
            ans=c*454
        elif b=='mg':
            ans=c*4535592
    return c,a,"{:.2e}".format(ans),b
def time(a,b,c):
    n=0
    if a=='hrs':
        if b=='mins':
            n=c*60
        elif b=='sec':
            n=c*360
    elif a=='mins':
        if b=='hrs':
            n=c/60
        elif b=='sec':
            n=c*60
    elif a=='sec':
        if b=='hrs':
            n=c/360
        elif b=='mins':
            n=c/60
    return n

def cubet(a):
    return 4*a*a

def cuboidc(l,b,h):
    return 2*h*(l+b)

def temp(a,b,c):
    ans=0
    if a.upper()=='K':
        if b.upper()=='C':
            ans=c-273
        elif b.upper()=='F':
            ans=((c*(9/5))-459.67)
    elif a.upper()=='C':
        if b.upper()=='K':
            ans=c+273.15
        elif b.upper()=='F':
            ans=((c*1.8)+32)
    elif a.upper()=='F':
        if b.upper()=='K':
            ans=((c+459.67)*(5/9))
        elif b.upper()=='C':
            ans=((c-32)/1.8)
    return ans

def madd(a,b,di):
    if di=='2*2':
        r=[[0,0],[0,0]]
    elif di=='2*3':
        r=[[0,0,0],[0,0,0]]
    elif di=='3*2':
        r=[[0,0],[0,0],[0,0]]
    elif di=='3*3':
        r=[[0,0,0],[0,0,0],[0,0,0]]
    elif di=='3*1':
        r=[[0],[0],[0]]
    elif di=='1*3':
        r=[[0,0,0]]
    elif di=='4*4':
        r=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    else:
        print('INVALID INPUT!!!')
    for i in range(len(r)):
        for j in range(len(r[0])):
            r[i][j]=a[i][j]+b[i][j]

def mmultiply(a,b,di):
    if di=='2*2':
        r=[[0,0],[0,0]]
    elif di=='2*3':
        r=[[0,0,0],[0,0,0]]
    elif di=='3*2':
        r=[[0,0],[0,0],[0,0]]
    elif di=='3*3':
        r=[[0,0,0],[0,0,0,],[0,0,0]]
    elif di=='1*3':
        r=[[0,0,0]]
    elif di=='3*1':
        r=[[0],[0],[0]]
    elif di=='4*4':
        r=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    else:
        print('invalid input!!!')
    for i in range(len(r)):
        for j in range(len(r[0])):
            for k in range(len(b)):
                r[i][j]+=a[i][k]*b[k][j]
    return r

def msub(a,b,di):
    if di=='2*2':
        r=[[0,0],[0,0]]
    elif di=='2*3':
        r=[[0,0,0],[0,0,0]]
    elif di=='3*2':
        r=[[0,0],[0,0],[0,0]]
    elif di=='3*3':
        r=[[0,0,0],[0,0,0],[0,0,0]]
    elif di=='1*3':
        r=[[0,0,0]]
    elif di=='3*1':
        r=[[0],[0],[0]]
    elif di=='4*4':
        r=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,]]
    else:
        r=[]
    if r==[]:
        return 'INVALID INPUT!!!'
    else:
        for i in range(len(r)):
            for j in range(len(r[0])):
                r[i][j]=a[i][j]-b[i][j]
        return r

def transpose(a,di):
    if di=='2*2':
        r=[[0,0],[0,0]]
    elif di=='2*3':
        r=[[0,0],[0,0],[0,0]]
    elif di=='3*2':
        r=[[0,0,0],[0,0,0]]
    elif di=='3*3':
        r=[[0,0,0],[0,0,0],[0,0,0]]
    elif di=='1*3':
        r=[[0],[0],[0]]
    elif di=='3*1':
        r=[[0,0,0]]
    elif di=='4*4':
        r=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,]]
    else:
        r=[]
    if r==[]:
        return 'INVALID INPUT'
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                r[j][i]=a[i][j]
        return r

def inverse(a):
    print(list(map(list,zip(*a))))
