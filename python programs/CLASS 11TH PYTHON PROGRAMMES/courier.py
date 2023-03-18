  #post office ke liye program
w=float(input('Enter weight of packet in grams:'))
d=float(input('Enter distance in KMS:'))
if w<=50:
    t=25
elif w>50 and w<=200:
      t=50
elif w>200:
      ext=w-200
      t=50+(ext*1)
      pass
if d<100:
      s=5
elif d>=100 and d<=300:
      s=15
elif d>300:
      ex=d-300
      s=20+(ex*1)
tot=t+s
print('You have to pay RS. :',tot)
      
