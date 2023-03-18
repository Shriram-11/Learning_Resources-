import csv
f=open('standings.txt','r')
f1=open('stats1.csv','w')
s=csv.writer(f1)
s.writerow(['POS','NAME','CODE','ORIGIN','TEAM','POINTS'])
l1=[]
a=f.read()
b=a.split('?')
for c in b:
    s.writerow(c.split(','))
f1.close()
