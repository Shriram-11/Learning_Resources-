import mymath
import math
print('DO YOU WANT TO USE THE CALCULATOR? ')
dec=input('YES/NO---:')
while dec.upper()=='YES':
    f=open('code.txt','r')
    print(f.read())
    f.close()   
#SIMPLE CALCULATION SECTION
    a1=int(input('Choose the operation you want to perform :'))
    if a1==0:
        r=eval(input('Enter arithematic expresion using operands (+,-,*,/)'))
        print(r)
#AREA SECTION
    elif a1==1:
        print("""Choose the type of surface of which of which you want to find the area:
SQUARE, RECTANGLE, CIRCLE, CUBE ,CUBOID, SPHERE, HEMISPHERE, CONE, CYLINDER, FRUSTUM""")
        a=input('ENTER CHOSEN SURFACE:')
        if a.upper()=='SQUARE':
            s=eval(input('Enter lenght of the side (in metres)'))
            ars=mymath.squarea(s)
            print(ars,'m^2')
        elif a.upper()=='RECTANGLE':
            l=eval(input('ENTER LENGHT (im metres)'))
            b=eval(input('ENTER BREADTH (in metres)'))
            print(mymath.rectanglea(l,b))
        elif a.upper()=='CIRCLE':
            r=eval(input('ENTER RADIUS(in metres ):'))
            print(mymath.circlea(r))
        elif a.upper()=='CUBE':
            s=eval(input('ENTER LENGHT OF SIDE(in metres)'))
            ar=input('LSA OR TSA?')
            if ar.upper=='LSA':
                print(mymath.cubet(s))
            elif ar.upper()=='TSA':
                print(mymath.cubea(s))
        elif a.upper()=='CUBOID':
            l=eval(input('LENGHT:'))
            b=eval(input('BREADTH:'))
            h=eval(input('HEIGHT:'))
            rec=input('LSA or TSA?')
            if rec.upper()=='TSA':
                print(mymath.cuboida(l,b,h))
        elif a.upper()=='CONE':
            r=eval(input('RADIUS='))
            do=input('DO U KNOW THE SLANT HEIGHT:')
            if do.upper()=='YES':
                l=eval(input('ENTER SLANT HEIGHT:'))
                c=input('CSA or TSA:')
                if c=='TSA':
                    print(mymath.conet(r,l))
                else:
                    print(mymath.conec(r,l))
            else:
                h=eval(input('ENTER HEIGHT:'))
                l=mymath.slantheightc(r,h)
                c=input('CSA or TSA:')
                if c=='CSA':
                    print(mymath.conec(r,l))
                else:
                    print(mymath.conet(r,l))
        elif a.upper()=='CYLINDER':
            c1=eval(input('RADIUS='))
            c2=eval(input('HEIGHT='))
            c3=input('CSA OR TSA:')
            if c3=='CSA':
                print(mymath.cylinderc(c1,c2))
            else:
                print(mymath.cylindert(c1,c2))
        elif a.upper()=='HEMISPHERE':
            r=eval(input('RADIUS='))
            c=input('CSA or TSA?')
            if c.upper()=='CSA':
                print(mymath.hemispherec(r))
            else:
                print(mymath.hemispheret(r))
        elif a.upper()=='SPHERE':
            r=eval(input('RADIUS:'))
            print(mymath.spheret(r))
        elif a.upper()=='FRUSTUM':
            r1=eval(input('r1='))
            r2=eval(input('r2='))
            slc=input('Do you the value of slant height:')
            cs=input('CSA or TSA')
            if slc=='YES':
                l=eval(input('l='))
                if cs=='CSA':
                    print(mymath.frustumc(r1,r2,l))
                else:
                    print(mymath.frustumt(r1,r2,l))
            else:
                h=eval(input('h='))
                l=mymath.slantheightf(r1,r2,h)
                if cs=='CSA':
                    print(mymath.frustumc(r1,r2,l))
                else:
                    print(mymath.frustumt(r1,r2,l))
        else:
            print('INVALID INPUT')
#VOLUME SECTION
    elif a1==2:
        print("""Choose the type of surface of which of which you want to find the area:
CUBE ,CUBOID, SPHERE, HEMISPHERE, CONE, CYLINDER, FRUSTUM""")
        d1=input('ENTER CHOSEN SURFACE:')
        if d1.upper()=='CUBE':
            d2=eval(input('ENTER LENGHT OF SIDE(in metres)'))
            print(mymath.cubev(d2))
        elif d1.upper()=='CUBOID':
            d3=eval(input('LENGHT:'))
            d4=eval(input('BREADTH:'))
            d5=eval(input('HEIGHT:'))
            print(mymath.cuboidv(d3,d4,d5))
        elif d1.upper()=='CONE':
            r1=eval(input('RADIUS='))
            h1=eval(input('ENTER HEIGHT:'))
            print(mymath.conev(r1,h1))
        elif d1.upper()=='CYLINDER':
            d6=eval(input('RADIUS='))
            d7=eval(input('HEIGHT='))
            print(mymath.cylinderv(d6,d7))
        elif d1.upper()=='HEMISPHERE':
            d9=eval(input('RADIUS='))
            print(mymath.hemispherev(d9))
        elif d1.upper()=='SPHERE':
            d0=eval(input('RADIUS:'))
            print(mymath.spherev(d0))
        elif d1.upper()=='FRUSTUM':
            e=eval(input('r1='))
            e1=eval(input('r2='))
            e2=eval(input('h='))
            print(mymath.frustumv(e,e1,e2))
        else:
            print('!!!INVALID INPUT!!!')
#TRIGNOMETRIC SECTION
    elif a1==3:
        e3=""" CHOOSE AMONG:
SIN ,COS ,TAN ,COT ,SEC ,COSEC"""
        print(e3)
        e4=input('Which function?')
        e5=eval(input('A='))
        theta=math.radians(e5)
        if e4=='SIN' or e4=='sin':
            print(math.sin(theta))
        elif e4=='COS' or e4=='cos':
            print(math.cos(theta))
        elif e4=='TAN' or e4=='tan':
            e7=math.cos(theta)
            if e7==0:
                print('NOT DEFINED')
            else:
                print(math.tan(theta))
        elif e4.upper()=='COT':
            e7=math.tan(theta)
            if e7==0:
                print('NOT DEFINED')
            else:
                print(math.pow(e7,-1))
        elif e4.upper()=='SEC':
            e7=math.cos(theta)
            if e7==0:
                print('not defined')
            else:
                print(math.pow(e7,-1))
        elif e4.upper()=='COSEC':
            e7=math.sin(theta)
            if e7==0:
                print('NOT DEFINED')
            else:
                print(math.pow(e7,-1))
        else:
            print('INVALID INPUT')
#VECTOR SECTION
    elif a1==5:
        print(""" CHOOSE AMONG:
RESULTANT VECTOR,VECTOR ADDITION , VECTOR PRODUCT""")
        e8=input('YOUR CHOSEN OPERATION:')
        if e8=='RESULTANT VECTOR':
            v=eval(input('ENTER IN FORMAT (VECTOR1,VECTOR2,ANGLE(IN DEG))'))
            v1,v2,t=v
            res=mymath.vectorres(v1,v2,t)
            di=vectordir(v1,v2,t)
            print('Resultant vector=',res,'Direction=',di)
        elif e8=='VECTOR ADDITION':
            print('ENTER IN FORMAT [Ax,Ay,Az]')
            f=eval(input("VECTOR 1="))
            f1=eval(input("VECTOR 2="))
            d=mymath.vectoradd(f,f1)
            print(d[0],'i',d[1],'j',d[2],'k')
        elif e8=='VECTOR PRODUCT':
            f2=input('VECTOR PRODUCT USING ANGLE OR CARTESIAN FORM')
            if f2=='CARTESIAN FORM':
                print('ENTER IN FORMAT [Ax,Ay,Az]')
                f=eval(input("VECTOR 1="))
                f1=eval(input("VECTOR 2="))
                f3=input('DOT OR CROSS')
                if f3=='DOT':
                    d=mymath.vectordot1(f,f1)
                    print(d[0],'i',d[1],'j',d[2],'k')
                elif f3=='CROSS':
                    d=mymath.vectorcross1(f,f1)
                    print(d[0],'i',d[1],'j',d[2],'k')
                else:
                    print('ERROR')
            elif f2=='ANGLE':
                f=eval(input('A='))
                f1=eval(input('B='))
                f4=eval(input('ANGLE='))
                f3=input('DOT OR CROSS')
                if f3=='DOT':
                    d=mymath.vectordot2(f,f1,f4)
                    print(d)
                elif f3=='CROSS':
                    d=mymath.vectorcross2(f,f1,f4)
                    print(d)
                else:
                    print('ERROR')
#QUADRATIC SECTION
    elif a1==4:
        print("ax^2+bx+c")
        a=eval(input('a='))
        b=eval(input('b='))
        c=eval(input('c='))
        d=math.pow(b,2)-(4*a*c)
        if d>0:
            r1=((-b+(math.sqrt(d)))/(2*a))
            r2=((-b+(math.sqrt(d)))/(2*a))
        elif d==0:
            r1=((-b)/(2*a))
            r2=((-b)/(2*a))
        else:
            r1=((-b+(cmath.sqrt(d)))/(2*a))
            r2=((-b+(cmath.sqrt(d)))/(2*a))
        print(r1,r2)
#MATRIX SECTION
    elif a1==6:
        print("""MATRIX SHOULD BE ENTERED IN FORM A=[[R1],[R2],[R3]......]
R DETERMINES ROW OF A MATRIX""")
        di=input("""SELECT DIMENSION
2*2,3*3,1*2,2*1,2*3 and 3*2:""")
        print('''OPERATIONS AVAILABLE:
ADD ,SUBTRACT ,MULTIPLY ,TRANSPOSE AND INVERSE''')
        op=input('SELECT OPERATION:')
        if op.upper()=='ADD':
            a=eval(input('MATRIX A:'))
            b=eval(input('MATRIX B:'))
            print(mymath.madd(a,b,di))
        elif op.upper()=='MULTIPLY':
            a=eval(input('MATRIX A:'))
            b=eval(input('MATRIX B:'))
            print(mymath.mmultiply(a,b,di))
        elif op.upper()=='SUBTRACT':
            a=eval(input('MATRIX A:'))
            b=eval(input('MATRIX B:'))
            print(mymath.msub(a,b,di))
        elif op.upper()=='TRANSPOSE':
            a=eval(input('MATRIX:'))
            print(mymath.transpose(a,di))
        elif op.lower()=='inverse':
            a=eval(input('MATRIX:'))
            print(mymath.inverse(a))        
#lcm
    elif a1==8:
        r1=int(input('a='))
        r2=int(input('b='))
        print(mymath.lcm(r1,r2))
#hcf
    elif a1==9:
        r1=int(input('a='))
        r2=int(input('b='))
        print(mymath.hcf(r1,r2))
#npr
    elif a1==10:
        n=int(input('n='))
        r=int(input('r='))
        print(mymath.npr(n,r))
#ncr
    elif a1==11:
       n=int(input('n='))
       r=int(input('r='))
       print(mymath.ncr(n,r))
#factorial
    elif a1==12:
        n=int(input('n='))
        print(mymath.fact(n))
#ceil
    elif a1==13:
        i=int(input('ENTER INTEGER:'))
        print(math.ceil(i))
#x^n
    elif a1==14:
        x=eval(input('x='))
        n=eval(input('n='))
        print(math.pow(x,n))
#log
    elif a1==15:
        z=eval(input('x='))
        b=eval(input('base='))
        print(math.log(z,b))
#unit conversions
    elif a1==16:
        d=input('Choose between lenght ,time ,mass or temperature:')
        if d.upper()=='LENGHT':
            print('''AVAILABLE UNITS ARE:
km ,m ,cm ,mm ,nm ,miles ,yards ,inches ,feets and nautical miles''')
            a=input('UNIT OF VALUE:')
            b=input('UNIT IN WHICH YOU WANT THE VALUE:')
            c=eval(input('value:'))
            print(mymath.lenghts(a,b,c))
        elif d.upper()=='MASS':
            a=input('UNIT OF THE VALUE:')
            b=input('UNIT IN WHICH YOU WANT THE VALUE:')
            c=eval(input('VALUE:'))
            print(mymath.mass(a,b,c))
        elif d.upper()=='TIME':
            print('''AVAILABLE UNITS ARE:
hrs ,mins and sec''')
            a=input('UNIT OF VALUE:')
            b=input('UNIT IN WHICH YOU WANT THE VALUE')
            c=eval(input('VALUE:'))
            print(mymath.time(a,b,c))
        elif d.upper()=='TEMPERATURE':
            print('''AVAILABLE UNITS ARE:
K ,C and F''')
            a=input('UNIT OF VALUE:')
            b=input('UNIT IN WHICH YOU WANT IT TO BE CHANGED:')
            c=eval(input('VALUE:'))
            print(mymath.temp(a,b,c))
#square root
    elif a1==17:
        sqr=eval(input('ENTER NUMBER:'))
        print(math.sqrt(sqr))
#cuberoot
    elif a1==18:
        cur=eval(input('ENTER NUMBER:'))
        print(math.pow(cur,1/3))
#nth root
    elif a1==19:
        nth=eval(input('ENTER NUMBER:'))
        n=eval(input('N='))
        print(math.pow(nth,1/n))
#square
    elif a1==20:
        sq=eval(input('ENTER NUMBER:'))
        print(math.pow(sq,2))
#cube
    elif a1==21:
        cu=eval(input('ENTER NUMBER:'))
        print(math.pow(cu,3))
    elif a1==22:
        d=input('''CHOOSE FROM THE FOLLOWING:
SIN COS TAN''')
        q=eval(input('x='))
        if d.upper()=='SIN':
            a=math.asin(q)
            print(math.degrees(a))
        elif d.upper()=='COS':
            a=math.acos(q)
            print(math.degrees(a))
        elif d.upper()=='TAN':
            a=math.atan(q)
            print(math.degrees(a))
        else:
            print('invalid input')
    else:
        print('INVALID INPUT!!! CODE---',a1,'''--- DOES NOT EXIST
CHOOSE FROM THE GIVEN TABLE ONLY''')
    dec=input('continue:')

print(''' BY:
NAME: SHRIRAM NAIK
CLASS: 12TH B
ROLL NO. : 18600360''')
#THE END .......
