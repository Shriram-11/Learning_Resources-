#write a menudriven python program to implement the list of movies with follwing functions
'''
add, serach, display all,remove all occ a movie
'''

movies=[]
def add():
    m=eval(input("Enter movie details [movies_name,year,rating]:"))
    movies.append(m)
def search():
    m=input("Enter movie name:")
    for a in movies:
        if a[0].lower()==m.lower():
            print("Present\n",a)
            break

    else:
        print("not present")
def  display():
    if len(movies)==0:
        print("No movies")
        return
    for m in movies:
        print(m)

def remove_occ():
    m=input("Enter movie name:")
    for a in movies:
        if a[0].lower()==m.lower():
            movies.remove(a)

def main():
    while True:
        choice=int(input('Choices are:\n1. Add   2. Search  3. Remove  4.  Display All   5. Exit\nEnter Choice:'))
        if choice==1:
            add()
        elif choice==2:
            search()
        elif choice==3:
            remove_occ()
        elif choice==4:
            display()
        elif choice==5:
            print("Bye!")
            break
        else:
            print("Invalid Input")

if __name__=='__main__':
    main()

