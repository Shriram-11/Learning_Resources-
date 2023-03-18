def c(p,q=30):
    p=p+q
    q=p-q
    print(p,'#',q)
    return p
r=150
s=100
r=c(r,s)
print(r,'#',s)
s=c(s)








"""#1
def count(x,y,z):
    for a in range(x,y,z):
        print(a)

x=int(input('start:'))
y=int(input('stop:'))
z=int(input('stop:'))
print(count(x,y,z))

#2
def countnow(a):
    for b in a:
        if len(b)>=5:
            print(b)

a=eval(input('enter list of spaces:'))
print(countnow(a))

#3
def execmain():
    x=int(input('Enter a number:'))
    if abs(x)==x:
        print('You have entered a positive number')
    else:
        x*=-1
        print('Number made positive:',x)
execmain()

#4

def Alter(P=15,Q=10):
    P=P*Q
    Q=P/Q
    print(P,'#',Q)
    return Q
A=100
B=200
A=Alter(A,B)
print(A,'$',B)
B=Alter(B)
print(A,'$',B)
A=Alter(A)
print(A,'$',B)
def checval():
    x=int(input('Enter a number:'))
    if x%2==0:
        print('even')
    elif x<0:
        print('number should be positive:')
    else:
        print('odd')
checval()

def main():
    moves=[11,22,33,44]
    queen=moves
    moves[2]+=22
    l=len(moves)
    for i in range(len(moves)):
        print(queen[l-i-1],moves[i])
main()

a=[11,22,33,44]
b=a
a[2]+=22
print(a,b)

def l(m):
    n=''
    c=0
    for i in m:
        if c%2!=0:
            n=n+str(c)
        else:
            if i.islower():
                n=n+i.upper()
            else:
                n=n+i
        c+=1
    n=n+m[:1]
    print(n)
l('sTUdeNT')"""

