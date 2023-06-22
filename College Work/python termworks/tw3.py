'''
Write a python program to read the books information from the user and store it in a CSV file containing rows in the following format:
bookNo,title,author,price
Develop a menu driven program with following options
1. Search the book by author
2. Search Nooks below a specified price (!<0)
3. Search books where the title contain ceratin word
4. Exit
'''

import csv

class PriceLess(Exception):
    pass
def add_book():
    book_no = input("Enter book number: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_no, title, author, price])
    print("Book information added successfully!")

def search_by_author():
    author = input("Enter author name: ")
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2].lower() == author.lower():
                print(", ".join(row))

def search_below_price():
    price_limit = float(input("Enter price limit: "))
    try:
        if price_limit<0:
            raise PriceLess
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if float(row[3]) < price_limit:
                    print(", ".join(row))
    except PriceLess:
        print("Price Limit Cannot be less than 0\n")
        
    

def search_by_title():
    keyword = input("Enter keyword: ")
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if keyword.lower() in row[1].lower():
                print(", ".join(row))

def main():
        n=int(input("Enter no. of books you want to add:"))
        for i in range(n):
            add_book()
        while True:
            print('''\nMenu:
        1. Search books by author
        2. Search books below a specified price
        3. Search books by title
        4. Exit''')
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                search_by_author()
            elif choice == '2':
                search_below_price()
            elif choice == '3':
                search_by_title()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
