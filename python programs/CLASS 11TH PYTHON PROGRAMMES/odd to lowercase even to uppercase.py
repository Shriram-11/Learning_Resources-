#program to convert a string odd charactes to lowercase and even charaters to uppercase
s=input('Enter a string:')
s2=''
for a in range(len(s)):
    if a%2==0:
        s2=s2 + s[a].upper()
    else:
        s2=s2 + s[a].lower()
print('CoNvErTeD StRiNg')
print(s2)
