n=int(input('Enter a number:'))
isprime=True
for x in range(2,n):
      if n%x==0:
            isprime=False
            break
if isprime:
      print(n,'is a prime no.')
else:
      print(n,'is not a prime no.')
