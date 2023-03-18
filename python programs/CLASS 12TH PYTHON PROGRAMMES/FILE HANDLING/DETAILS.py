import pickle
f=open('employ.dat','rb')
d={}
print('DETAILS OF EMPLOYEES')
try:
    while True:
        d=pickle.load(f)
        print(d)
except:
    f.close()
