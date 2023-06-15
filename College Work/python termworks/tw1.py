queue=[]

def enqueue(a):
    queue.append(a)

def display():
    if len(queue)<0:
        print("Empty List")
        return
    print("Queue\n")
    print(queue[0],"Front")
    for i in range(1,len(queue)-1):
        print(queue[i])
    print(queue[-1],"Rear\n")
    
def dequeue():
    if len(queue)>0:
        print("Removed",queue.pop(0))
    else:
        print("Underflow")

def qFront():
    if len(queue)>0:
        print("Front:",queue[0])
    else:
        print("Underflow")
        
def qRear():
    if len(queue)>0:
        print("Rear:",queue[-1])
    else:
        print("Underflow")
def main():
    while(1):
        choice=int(input("Choices\n1. Enqueue  2. Dequeue   3.   Display\n4. Queue Front     5. Queue Rear      6. Exit\nEnter Choice:"))
        if choice==1:
            enqueue(input("Enter element to add:"))
        elif choice==2:
            dequeue()
        elif choice==3:
            display()
        elif choice==4:
            qFront()
        elif choice==5:
            qRear()
        elif choice==6:
            print("Byee!")
            break
        else:
            print("Invalid Option")
        print()
if __name__ == '__main__':
    main()