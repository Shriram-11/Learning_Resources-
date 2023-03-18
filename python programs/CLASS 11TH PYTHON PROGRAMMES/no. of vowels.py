#program to find no. of vowels in a string
s=input('Enter a string:')
count=0
for a in s:
    if a in 'aeiou' or a in 'AEIOU':
        count=count+1
print('Total no. of vowels in',s,'are ',count)
