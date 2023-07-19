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
    """
    Function to add a book to the CSV file.
    """
    book_no = input("Enter book number: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_no, title, author, price])
        
    print("Book information added successfully!")

def search_by_author():
    """
    Function to search books by author.
    """
    f=0
    author = input("Enter author name: ")
    
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2].lower() == author.lower():
                print("Book No.:",row[0]," Name:",row[1]," Author:",row[2]," Price:",row[3])
                f=1
        if f==0:
            print("Book not found")

def search_below_price():
    """
    Function to search books below a specified price.
    """
    price_limit = float(input("Enter price limit: "))
    
    try:
        if price_limit < 0:
            raise PriceLess
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            f=0
            for row in reader:
                if float(row[3]) < price_limit:
                    print("Book No.:",row[0]," Name:",row[1]," Author:",row[2]," Price:",row[3])
                    f=1
            if f==0:
                print("No book below specified price")
    except PriceLess:
        print("Price Limit Cannot be less than 0\n")

def search_by_title():
    """
    Function to search books by title.
    """
    keyword = input("Enter keyword: ")
    f=0
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if keyword.lower() in row[1].lower():
                print("Book No.:",row[0]," Name:",row[1]," Author:",row[2]," Price:",row[3])
                f=1
        if f==0:
            print("No book found conataining the word ",keyword)

def main():
    """
    Main function to run the program.
    """
    
    n = int(input("Enter the number of books you want to add: "))
     
    for i in range(n):
        add_book()
    print("Books Are:")
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
        
    while True:
        print('''\nMenu:
        1. Search books by author
        2. Search books below a specified price
        3. Search books by title
        4. Exit''')
        
        choice = input("Enter your choice (1-4): ")
        
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

