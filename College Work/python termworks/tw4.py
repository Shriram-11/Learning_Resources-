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

import sqlite3

# Create a database
conn = sqlite3.connect('products.sqlite')
cursor = conn.cursor()

# Create the products table
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (prodid INT PRIMARY KEY, name TEXT, quantity INT, price REAL)''')

# Function to insert records into the table
def insert_records(n):
    for _ in range(n):
        prodid = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                       (prodid, name, quantity, price))
    conn.commit()

# Insert records into the table
n = int(input("Enter the number of records to insert: "))
insert_records(n)

# Display all the records
cursor.execute("SELECT * FROM products")
records = cursor.fetchall()
print("Product ID\tName\t\tQuantity\tPrice")
for record in records:
    print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}\t\t{record[3]}")

# Delete a product by product ID
prod_id = int(input("Enter the product ID to delete: "))
cursor.execute("DELETE FROM products WHERE prodid = ?", (prod_id,))
conn.commit()

# Increase the price of products with price less than 50 by 10%
cursor.execute("UPDATE products SET price = price * 0.1 WHERE price < 50")
conn.commit()

# Display products with quantity less than 40
cursor.execute("SELECT * FROM products WHERE quantity < 40")
records = cursor.fetchall()
print("Products with quantity less than 40:")
print("Product ID\tName\t\tQuantity\tPrice")
for record in records:
    print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}\t\t{record[3]}")

# Close the connection
conn.close()
