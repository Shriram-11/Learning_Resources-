import pickle
f=open('employ.dat','wb')
op='Y'
e={}
while op.upper()=='Y':
    empno=int(input('Employee Number:'))
    fname=input('Employee Name:')
    sal=float(input('Salary'))
    e['EMPNO']=empno
    e['NAME']=fname
    e['SALARY']=sal
    pickle.dump(e,f)
    op=input('WANT TO ENTER MORE y/n?')
print('DATA ENTERED')
f.close()
