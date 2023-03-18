def x(b,stk):
    print( 'X shall play')
    x_input=int(input('Select a box (1-9): '))
    if x_input not in [1,2,3,4,5,6,7,8,9]:
        print('out of range')
        x(b,stk)
    elif x_input in stk:
        print('Repeated')
        x(b,stk)
    else:
        stk.append(x_input)
        b[x_input]='X'
        print(b)
        print(b[1],'|',b[2],'|',b[3])
        print('----------------')
        print(b[4],'|',b[5],'|',b[6])
        print('----------------')
        print(b[7],'|',b[8],'|',b[9])
        print('----------------')
    return b,stk

def o(b,stk):
    print('O shall play')
    o_input=int(input('Select a box (1-9): '))
    if o_input not in [1,2,3,4,5,6,7,8,9]:
        print('Value out of range')
        o(b,stk)
    elif o_input in stk:
        print('Repeated')
        o(b,stk)
    else:
        stk.append(o_input)
        b[o_input]='O'
        print(b[1],'|',b[2],'|',b[3])
        print('----------------')
        print(b[4],'|',b[5],'|',b[6])
        print('----------------')
        print(b[7],'|',b[8],'|',b[9])
        print('----------------')
    return b,stk


