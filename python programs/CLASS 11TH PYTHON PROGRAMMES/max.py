a=int(input('enter a number:'))
b=int(input('enter anothernumber:'))
num=int(input('pls enter another number'))
Max=a
if b>Max:
    Max=b
elif Max==a:
    pass
else num >Max:
    Max=num
elif Max==a:
print('the greatest number is',Max)
