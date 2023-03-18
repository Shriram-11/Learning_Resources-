import pickle
f=open('op.dat','wb')
op='Y'
e={}
while op.upper()=='Y':
    act=input('NAME OF OPERATION:')
    code=int(input('ENTER CODE:'))
    e['operation']=act
    e['code']=code
    pickle.dump(e,f)
    op=input('MORE?')
f.close()
