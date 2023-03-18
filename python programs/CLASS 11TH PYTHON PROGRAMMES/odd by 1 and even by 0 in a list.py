#program to read a list,replace even places with 0 and odd values by 1
lst=eval(input('Enter a list:'))
for a in range(len(lst)):
    if a%2==0:
        lst[a]=0
    else:
        lst[a]=1
print('updated list=',lst)
