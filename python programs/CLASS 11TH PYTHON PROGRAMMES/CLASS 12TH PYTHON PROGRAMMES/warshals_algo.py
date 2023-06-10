a=eval(input("Enter Matrix:"))
#D:\python programs\CLASS 12TH PYTHON PROGRAMMES\warshals_algo.py
def check(m):
    for l in m:
        if(len(l) == len(m)):
            continue
        else:
            print("Not in proper format")
            exit(0)

check(a)
print("Original Matrix:")

def printm(m):
    for c in m:
        for d in c:
            print(d,end="  ")
        print()

printm(a)

def warshall(a):
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
        print("Iteration:",k,"\n")
        printm(a)
        print("\n")
    return a

b=warshall(a)

print("Transitive Closure")

printm(b)

