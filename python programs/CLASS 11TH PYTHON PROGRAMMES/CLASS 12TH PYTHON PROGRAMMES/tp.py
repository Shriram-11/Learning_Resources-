limit=['*',1,'%',2,'&',6]
c1=0
s=''
l=0
for c in range(1,6,2):
    c1=c1+c
    s=s+limit[c-1]+'#'
    l=l+limit[c]
    print(c1,l,s)
