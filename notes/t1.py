# Python Program To read n names from the user store it in a list and write to a text file
# The program should also read the names from the text file and display them

names = []
n= int(input("Enter No.:"))
for i in range(n):
    names.append(input("Enter Name:")+'\n')
with open('sample.txt', 'w',newline="") as f:
    f.writelines(names)

with open('sample.txt', 'r') as f:
    print("Sample.txt content:")
    li=f.readlines()
    for i in li:
        print(i[:-1])
