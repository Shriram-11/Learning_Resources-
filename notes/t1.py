# Python Program To read n names from the user and write to a text file
# The program should also read the names from the text file and display them

with open('sample.txt', 'w',newline="") as f:
    while True:
        n=int(input("Enter a name:"))
        f.write(n)
        if input("Enter more? (y/n):").lower() != 'y':
            break
    f.close()

with open('sample.txt', 'r') as f:
    print("Sample.txt content:")
    li=f.readlines()
    for i in li:
        print(i)

