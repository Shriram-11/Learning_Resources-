# binary file handling system for strings
a = eval(input('ENTER:'))
b = int(input('Element to search:'))
# c=a.split()
a.sort()


def binarysearch(a, b, start, end):
    if end >= start:
        mid = int((start+end)/2)
        if b < a[mid]:
            return binarysearch(a, b, start, mid)
        elif b > a[mid]:
            return binarysearch(a, b, mid+1, end)
        else:
            return mid
    else:
        return -1


result = binarysearch(a, b, 0, len(a)-1)
if result == -1:
    print('!!!ERROR!!!')
else:
    print('FOUND AT INDEX:', result)
