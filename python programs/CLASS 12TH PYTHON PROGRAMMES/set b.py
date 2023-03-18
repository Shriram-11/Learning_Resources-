'''SET - B
1) Develop a python program to read a text file and display the total
number of lines words and characters.
Also Count and Display all words which starts with t or T
2) Using Python interface search an employee number in the EMPL
table of EMPLOYEE database of MySQL and display its details.'''

'''f=open('story.txt','r')
t=0
b=f.read()
l=len(b.split('\n'))
c=b.split()
w=len(c)
char=len(b)
print('Total lines:',l)
print('Total words:',w)
print('Total character:',char)
for i in b:
    if i[0]=='t' or i[0]=='T':
        t=t+1
print('Total words starting with t or T:',t)
'''

'''import mysql.connector as m
c=m.connect(host='localhost',charset='utf8',user='root',passwd='tiger',database='employee')
crsr=c.cursor()
e=int(input('ENTER EMPLOYEE NUMBER TO SEARCH:'))
crsr.execute('select* from empl where empno=%s;',(e,))
r=crsr.fetchall()
for a in r:
    print(r)'''
