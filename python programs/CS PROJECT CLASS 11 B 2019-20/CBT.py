#MCQ TEST 
print('This is a Computer Based Test')
print('INSTRUCTIONS:')
print('1. YOU HAVE TO CHOOSE BETWEEN PHYSICS,CHEMISTRY OR COMPUTER SCIENCE')
print('2. THE INPUTS MUST BE IN BLOCK LETTERS ONLY!!!')
print('3. THERE WILL BE 5 QUESTIONS')
print('   #FOR CORRECT ANS. YOU WILL BE AWARDED 4 marks')
print('   #FOR WRONG ANSWER 0.50 MARKS WILL BE DEDUCTED')
print('   #NO MARKS WILL BE DEDUCTED FOR UNATTEMPTED QUESTION')
print('4. ANSWERE ONLY IN A,B,C OR D AND TYPE NA IF YOU DO NOT WANT TO ATTEMPT')
marks=opt=0
tot=20
c='correct'
i='incorrect'
d='not attempted'
q1=q2=q3=q4=q5=''
name=input('NAME:')
roll=input('ROLL NUMBER:')
sub=input('SUBJECT:')
if sub=='PHY':
    print('1. Heat is associated with:')
    print('    A. K.E of random motion of molecules       B. K.E of orderly motion of molecules:')
    print('    C. potential energy                                      D. none of these')
    ap1=input('ANSWER:')
    if ap1=='A':
        opt=opt+4
        q1+=c
    elif ap1=='NA':
        opt=opt+0
        q1+=d
    else:
        opt=opt-0.5
        q1+=i
    print('2. Modulus of rigidity of ideal liquid is:')
    print('    A. infinity         B. 0           C.1        D. some finite non zero constant value')
    ap2=input('ANSWER:')
    if ap2=='B':
        opt+=4
        q2+=c
    elif ap2=='NA':
        opt+=0
        q2+=d 
    else:
        opt=opt-0.5
        q2+=i 
    print('3. Along a streamline the :')
    print('A. velocity of a fluid particle remains constant')
    print('B. velocity of all fluid particles passing a given poin is constant')
    print('C. speed of the fluid particle is constant        D. none of the above')
    ap3=input('ANSWER:')
    if ap3=='B':
        opt+=4
        q3+=c
    elif ap3=='NA':
        opt+=0
        q3+=d
    else:
        opt=opt-0.5
        q3+=i
    print('4. Boyle','s law is aplicable to ............ process. ')
    print('    A. ADIABATIC      B. ISOTHERMAL         C. ISOBARIC          D. ISOCHORIC')
    ap4=input('ANSWER')
    if ap4=='B':
        opt+=4
        q4+=c 
    elif ap4=='NA':
        opt+=0
        q4+=d
    else:
        opt=opt-0.5
        q4+=i
    print('5. Water waves produced by a motoboat are:')
    print('     A. neither longitudinal nor transverse       B. only longitudinal')
    print('     C. both longitudnal and tranverse              D. only transverse')
    ap5=input('ANSWER')
    if ap5=='C':
        opt+=4
        q5+=c
    elif ap5=='NA':
        opt+=0
        q5+=c
    else:
        opt=opt-0.5
        q5+=i
elif sub=='CS':
    print('1. What type of programming language is PYTHON:')
    print('    A. Compiled  B. opensource C. interperted D. both B and C')
    a1=input('ANSWER:')
    if a1=='D'or a1=='B' or a1=='C':
        opt+=4
        q1+=c
    elif a1=='NA':
        opt+=0
        q1+=d
    else:
        opt=opt-0.5
        q1+=i
    print('2. STRING is an ............. datatype.')
    print('A. mutable    B. immutable   C. both A and B     D. none of these')
    a2=input('ANSWER:')
    if a2=='B':
        opt+=4
        q2+=c
    elif a2=='NA':
        opt+=0
        q2+=d
    else:
        opt=opt-0.5
        q2+=i
    print('3. [1,2.3,2+1j,''hello''] is a:')
    print('A. list     B. tuple    C. dictionary    D. string')
    a3=input('ANSWER:')
    if a3=='A':
        opt+=4
        q3+=c
    elif a3=='NA':
        opt+=0
        q3+=d
    else:
        opt=opt-0.5
        q3+=i
    print('PRIDICT THE OUTPUT:')
    print(' a=''h')
    print(' b=2')
    print('print(a+b)')
    print('A. hh      B. h+2    C. error    D. none of these')
    a4=input('ANSWER:')
    if a4=='C':
        opt+=4
        q4+=c
    elif a4=='NA':
        opt+=0
        q4+=d
    else:
        opt=opt-0.5
        q4+=i
    print('5. What is the output of: print(6//3)')
    print('     A. 0        B. 2     C. error   D none of these ')
    a5=input('ANSWER:')
    if a5=='B':
        opt+=4
        q5+=c
    elif a5=='NA':
        opt+=0
        q5+=d
    else:
        opt=opt-0.5
        q5+=d
else:
    print('1. Metallic elements are described by their standard electrode potential, fusion enthalpy,')
    print('atomic size, etc. /The alkali metals are characterised by which of the following properties?')
    print(' A. High boiling point                B. High negative standard electrode potential ')
    print('C. High density                          D. Large atomic size')
    a1=input('ANSWER:')
    if a1=='B':
        opt=opt+4
        q1+=c
    elif a1=='NA':
        opt=opt+0
        q1+=d
    else:
        opt=opt-0.5
        q1+=i
    print('2.The element which exists in liquid state for a wide range of temperature and can be used')
    print('for measuring high temperature is:')
    print('A. Boron         B. Aluminium          C. Gallium       D.  Indium')
    a2=input('ANSWER:')
    if a2=='C':
        opt=opt+4
        q2+=c
    elif a2=='NA':
        q2+=d
        opt=opt+0
    else:
        opt=opt-0.5
        q2+=i
    print('3.The increasing order of reduction of alkyl halides with zinc and dilute HCl is:')
    print('A. R-Cl<R-I<R-Br     B. R-Cl<R-Br<R-I    C. R-I<R-Br<R-Cl    D. R-Br<R-I<R-Cl ')
    ac3=input('ANSWER:')
    if ac3=='B':
        opt=opt+4
        q3+=c
    elif ac3=='NA':
        opt=opt+0
        q3+=d
    else:
        opt=opt-0.5
        q3+=i
    print('4. Which of the following hydrides is electron-precise hydride? ')
    print('A. B2H6     B. NH3     C. H2O    D. CH4')
    ac4=('ANSWER:')
    if ac4=='D':
        opt=opt+4
        q4+=c
    elif ac4=='NA':
        opt=opt+0
        q4+=d
    else:
        opt=opt-0.5
        q4+=i
    print('5. Which of the following attain linear structure?')
    print('A. BeCl2   B. NO2    C. CS2     D.NCO+')
    ac5=input('ANSWER:')
    if ac5=='A':
        opt=opt+4
        q5+=c
    elif ac5=='NA':
        opt=opt+0
        q5+=d
    else:
        opt=opt-0.5
        q5+=i
marks=opt
per=(marks/tot)*100
print('YOUR RESULTS ARE:')
print('NAME:',name,'             ROLL NO.:',roll,'              SUBJECT:',sub)
print('QUESTION 1:',q1)
print('QUESTION 2:',q2)
print('QUESTION 3:',q3)
print('QUESTION 4:',q4)
print('QUESTION 5:',q5)
print('TOTAL MARKS SCORED:',marks,'          PERCENTAGE:',per)
if per>=40:
    r='PASS'
else:
    r='FAIL!!!!!!!'
print('OVERALL RESULT:',r)
z=input('For answer key type YES:')
if z=='YES':
    if sub=='PHY':
        q={1:'A',2:'B',3:'B',4:'B',5:'C'}
    elif sub=='CS':
        q={1:'D',2:'B',3:'A',4:'C',5:'B'}
    else:
        q={1:'B',2:'C',3:'B',4:'D',5:'B'}
print(q)
print('                                                      THANKYOU  ',name,'                           ')
#SHRIRAM NAIK
('PREPARED BY : SHRIRAM NAIK')
