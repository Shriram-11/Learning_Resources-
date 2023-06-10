'''SET - C
1) Develop a Python program that accepts Roll Number, Name and
Percentage of multiple students using dictionary and save the
information into a binary file. After accepting all records display
the contents of binary file on the screen.
2) Using Python interface display all records of EMPL table stored in
database EMPLOYEE in MySQL.'''

'''import pickle
f=open('STUFILE.DAT','wb')
c='Y'
while c.upper()=='Y':
    r=int(input('Enter roll no.:'))
    n=input('Enter name:')
    p=float(input('Enter percentage:'))
    pickle.dump([r,n,p],f)
    c=input('Press Y/y to enter more data:')

print('Data Entered')
f.close()

f1=open('STUFILE.DAT','rb')
try:
    while True:
        a=pickle.load(f1)
        print(a)
except:
    f1.close()
'''

'''import mysql.connector as m
c=m.connect(host='localhost',charset='utf8',user='root',passwd='tiger',database='employee')
crsr=c.cursor()
crsr.execute('select* from empl;')
r=crsr.fetchall()
for a in r:
    print(a)'''
