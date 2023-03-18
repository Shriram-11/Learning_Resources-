n=int(input('enter a number :'))
for i in range(2,2//n):
   if n%i==0:
        print("the number",n,"is not a primr number")
        break
else:
    print("the number",n,"is a prime no.")
