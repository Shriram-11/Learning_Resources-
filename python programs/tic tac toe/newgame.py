import t1
def GAME():
    stk=[]
    count = 0
    canvas_blank = '''
        |   |
    --------------
        |   |
    --------------
        |   |
    '''
    r='Y'
    b={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

    #player names
    p1=input('Enter player 1\'s name:')
    p2=input('Enter player 2\'s name:')
    print(p1,'is X and',p2,'will play with O')
    #intitial canvas
    print(b[1],'|',b[2],'|',b[3])
    print('-------------')
    print(b[4],'|',b[5],'|',b[6])
    print('----------------')
    print(b[7],'|',b[8],'|',b[9])
    print()
    #game logic
    w=False
    while True:
        t1.x(b,stk)
        count+=1
        print()
        a=p1+'  Wins'
        o=p2+'  Wins'
        if b[1]==b[2]==b[3]=='X':
            print(a)
            w='T'
        elif b[4]==b[5]==b[6]=='X':
            print(a)
            w='T'
        elif b[7]==b[8]==b[9]=='X':
            print(a)
            w='T'
        elif b[1]==b[4]==b[7]=='X':
            print(a)
            w='T'
        elif b[2]==b[5]==b[8]=='X':
            print(a)
            w='T'
        elif b[3]==b[6]==b[9]=='X':
            print(a)
            w='T'
        elif b[1]==b[5]==b[9]=='X':
            print(a)
            w='T'
        elif b[3]==b[5]==b[7]=='X':
            print(a)
            w='T'
        elif b[1]==b[2]==b[3]=='Y':
            print(o)
            w='T'
        elif b[4]==b[5]==b[6]=='Y':
            print(o)
            w='T'
        elif b[7]==b[8]==b[9]=='Y':
            print(o)
            w='T'
        elif b[1]==b[4]==b[7]=='Y':
            print(o)
            w='T'
        elif b[2]==b[5]==b[8]=='Y':
            print(o)
            w='T'
        elif b[3]==b[6]==b[9]=='Y':
            print(o)
            w='T'
        elif b[1]==b[5]==b[9]=='Y':
            print(o)
            w='T'
        elif b[3]==b[5]==b[7]=='Y':
            print(o)
            w='T'
        if w=='T':
            break
        t1.o(b,stk)
        count+=1
        print()
   

