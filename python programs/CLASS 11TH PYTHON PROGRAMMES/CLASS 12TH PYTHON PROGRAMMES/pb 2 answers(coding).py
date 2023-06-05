
def cf(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    for j in a:
        c=l.count(j)
        print('Frequency of',j,': ',c)

lst=[1,2,2,3,4,4,5]
cf(lst)
            
        
