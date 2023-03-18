import random
print('''THIS IS A NUMBER GUESSING GAME
The rules are given below
1.ENTER A NUMBER
2.IF THE NUMBER IS GREATER THAN THE NO. YOU CHOOSE THE IT WILL PRINT (HIGH)
3.IF THE NUMBER YOU CHOOSE IS SMALLER THEN IT WILL PRINT (LOW)''')
num=random.randint(1,99)
n=int(input('CHOOSE A NUMBER BETWEEN 1-99:'))
while num!=n:
    if n<num:
        print('LOW')
        n=int(input('CHOOSE A NUMBER BETWEEN 1-99:'))
    elif n>num:
        print('HIGH')
        n=int(input('CHOOSE A NUMBER BETWEEN 1-99:'))
    else:
        break
print('''VAMOS
YOU GUESSED THE NUMBER''')
