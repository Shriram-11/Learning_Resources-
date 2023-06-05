stack = []
ch = int(input(
    "Choose operations:\n1. Push\n2. Pop\n3. Print\n4. Print top element\n5. exit\n"))


def push():
    a = eval(input("Enter the element to push\n"))
    stack.append(a)
    print("Element added")


def POP():
    print("Element deleted\n", stack.pop())


def top():
    print(stack[-1])


def ifEmpty():
    if len(stack) == 0:
        print("Stack is empty\n")
    else:
        print("Stack is not empty\n")
        print(stack)


while ch != 5:
    if ch == 1:
        push()
    elif ch == 2:
        POP()
    elif ch == 3:
        ifEmpty()
    elif ch == 4:
        top()
    else:
        print("Invalid Input")
    ch = int(input(
        "Choose operations:\n1. Push\n2. Pop\n3. Print\n4. Print top element\n5. exit\n"))
