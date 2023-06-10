'''SET - E
1) AIM - Develop a python program to accept Employee Number,
Employee Name, Salary and Department into a List, and save the
details of employees into binary file named COMPANY.DAT. After
creating the binary file accept employee number from the user
and search it in the binary file and display the information of the
employee.
2) Using Python interface display all records of EMPL table stored in
database EMPLOYEE in MySQL.'''

import mysql.connector as m
import pickle
f = open('student.dat', 'wb')
c = 'Y'
while c.upper() == 'Y':
    e = int(input('enter employee no.:'))
    n = input('enter employee name:')
    s = float(input('enter salary:'))
    d = input('Enter department:')
    pickle.dump([e, n, s, d], f)
    c = input('press Y/y to continue:')

f.close()

f1 = open('student.dat', 'rb')
emp = int(input('Enter employee no. to search:'))
found = False
try:
    while True:
        a = pickle.load(f1)
        if a[0] == emp:
            print(a)
            found = True
            break
except:
    if found == False:
        print('Not Found')

    f1.close()

c = m.connect(host='localhost', charset='utf8', user='root',
              passwd='tiger', database='employee')
cr = c.cursor()
cr.execute('select*from empl;')
r = cr.fetchall()
for a in r:
    print(a)
