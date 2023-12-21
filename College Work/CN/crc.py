def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword


def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword, remainder


def manipulate(data, idx):
    if idx >= len(data):
        print("Invalid index")
        return data
    if data[idx] == "0":
        data = data[:idx] + "1" + data[idx+1:]
    else:
        data = data[:idx] + "0" + data[idx+1:]
    return data


def checksum(rem):
    if "1" in rem:
        print("Data was manipulated")
    else:
        print("Correct data recieved")


data = input("Enter data you want to send->")
key = input("Enter the divisor in binary:")
ans, rem = encodeData(data, key)
print("Encoded data:", ans)
ch = int(input("Enter choice\n1. Error free transmission\n2. Error simulation"))


if ch == 1:
    remainder = mod2div(ans, key)
    print("Code word:", ans, "\t", remainder)
    checksum(remainder)
elif ch == 2:
    idx = int(input("Enter the index of bit you want to manipulate:"))
    ndata = manipulate(ans, idx)
    rem = mod2div(ndata, key)
    print("Manipulated Code word", ndata, "\tRemainder:", rem)
    checksum(rem)
