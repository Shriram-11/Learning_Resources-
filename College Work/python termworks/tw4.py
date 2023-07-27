'''
Write a python program to perfoem the following
a) Create a database named products.sqlite
b) Create  a table named products with following fields:
    prodid:INT
    name:Text
    quantity:INT
    price:Float
c) Insert n records into the table
d) Display the recordset after fetching all the rows
e) Delete the product whose product id is entered by user
f) Increase the price of all the products whose current price is less than 50 by 10%
g) Display all the products whose quantity is less than 40
'''

import sqlite3 as sq
from contextlib import closing

#creating databse co
conn=sq.connect("products1.sqlite")
if conn:
    print("Connected")
else:
    print("Connection Failed")
    exit()

#creating a table 
def create_table():
    with closing(conn.cursor()) as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS products
                        (prodid INT PRIMARY KEY, name TEXT, quantity INT, price REAL)''')

#function to enter n records into table
def insertRec(n):
    with closing(conn.cursor()) as cursor:
        for _ in range(n):
            prodid=int(input("Enter Production ID: "))
            name=input("Enter Product Name: ")
            quantity=int(input("Enter record of quantity: "))
            price=float(input("Enter Product price: "))
            cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                        (prodid, name, quantity, price))
        
    conn.commit()


#display all records
def displayALL():
    with closing(conn.cursor()) as cursor:
        cursor.execute("sELECT * FROM products")
        records=cursor.fetchall()
        print("Product ID\tName\t\tQuantity\tPrice")
        for record in records:
            print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}\t\t{record[3]}")

# Delete a product by product ID
def delPro():
    with closing(conn.cursor()) as cursor:
        prod_id = int(input("Enter the product ID to delete: "))
        cursor.execute("DELETE FROM products WHERE prodid = ?", (prod_id,))
        conn.commit()
        displayALL()

# Increase the price of products with price less than 50 by 10%
def incPri():
    with closing(conn.cursor()) as cursor:
        cursor.execute("UPDATE products SET price = price + price * 0.1 WHERE price < 50")
        conn.commit()
        displayALL()

#Display products with quantity less than 40
def disQut():
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM products WHERE quantity<40")
        records=cursor.fetchall()
        print("Products with quantity less than 40:")
        print("Product ID\tName\t\tQuantity\tPrice")
        for record in records:
            print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}\t\t{record[3]}")


def main():
    create_table()
    while(1):
        print("Enter choice\n1 Insert n values\n2 Display All records\n3 Delete a product\n4 Increase price of product if its price is less than 50\n5 Display products with quantity less than 40\n6 Exit ")
        c=int(input())

        if(c==1):
            n=int(input("Enter number of records: "))
            insertRec(n)
        elif(c==2):
            print("Products Database: ")
            displayALL()
        elif(c==3):
            delPro()
        elif(c==4):
            print("Increased prices: ")
            incPri()
        elif(c==5):
            print("Products who have less quantity than 40: ")
            disQut()
        elif(c==6):
            print("Database closed sucessfully")
            # Close the connection
            conn.close()
            exit()



if __name__=='__main__':
    main()

