#program to calculate attendence
n=int(input('Enter total working days:'))
a=int(input('Enter athe number of days you were present:'))
p=(a/n)*100
if p<75:
      print('Not ELIGIBLE')
elif p>90:
      print('ELIGIBLE TO WRITE EXAM')
print('YOUR ATTENDENCE IS :',p,'%')
      
