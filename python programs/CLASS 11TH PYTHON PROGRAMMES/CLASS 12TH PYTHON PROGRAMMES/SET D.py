'''SET - D
1) Develop a Python program to create csv file named EMP.csv to
store employee no, name and salary of more than one employees.
2) Develop a python program to create STUDENT table in current
database of MySQL and insert data using python interface'''
'''
import csv
f=open('EMP.csv','w',newline='')
c=csv.writer(f)
ch='Y'
while ch.upper()=='Y':
    e=int(input('Enter employee no.:'))
    n=input('Enter employee name:')
    s=float(input('Enter salary:'))
    a=[e,n,s]
    c.writerow(a)
    ch=input('PRESS Y/y TO ENTER MORE DATA:')
f.close()
'''
'''import mysql.connector as m
c=m.connect(host='localhost',charset='utf8',user='root',passwd='tiger',database='employee')
cr=c.cursor()'''
q='''create table st (ROLL_NO INT(3) PRIMARY KEY,NAME VARCHAR(25),PERCENTAGE DECIMAL(7,0),
DOB DATE);'''
'''cr.execute(q)
c.commit()
ch='Y'
while ch.upper()=='Y':
    r=int(input('Enter roll no.:'))
    n=input('Enter name:')
    p=float(input('Enter percentage:'))
    d=input('Enter DOB (yyyy-mm-dd):')
    t=(r,n,p,d)
    cr.execute('insert into student values(%s,%s,%s,%s);',t)
    ch=input('Press Y/y to continue:')

cr.execute('select* from st;')
w=cr.fetchall()
for i in w:
    print(i)
c.commit()
c.close()
'''
