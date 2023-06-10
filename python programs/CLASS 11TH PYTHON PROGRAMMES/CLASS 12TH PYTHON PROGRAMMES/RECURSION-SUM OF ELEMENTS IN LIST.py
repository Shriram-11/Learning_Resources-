#RECURSION-SUM OF ELEMENTS IN A LIST
def lst_sm(a):
    sm=0
    for b in a:
        sm=sm+int(b)
    return sm
a=eval(input('Enter a list of number:'))
print('Sum of integers in the given list is:',lst_sm(a))
