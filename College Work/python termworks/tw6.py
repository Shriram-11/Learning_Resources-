'''
Create a system using Object composition and encapsulation concepts that allows customers to place orders for products.
The program consistes of three classes: Customer,Order and Product.
The customer class allows customers to place orders and it stores cutomers name , email and a list of their orders.
The orders class stores orderID and a list of products and has a method to calculate total price of an order. The product class stores name 
and price of a product
'''


class Product():
    def __init__(self,pname,price):
        self.__pname = pname
        self.__price = price
    
    def getPrice(self):
        return self.__price
    def getName(self):
        return self.__pname
class Order():
    def __init__(self,orderID,products):
        self.__orderID = orderID
        self.__products = products
    def calculateTotal(self):
        total=0
        for prod in self.__products:
            total += prod.getPrice()
        return total
    def getOrderId(self):
        return self.__orderID
    def getProducts(self):
        return self.__products

class Customer():
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
        self.__orders=[]
    def getCname(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def getOrders(self):
        return self.__orders
    def placeOrders(self,order):
        self.__orders.append(order)
    def display(self):
        print(f"Name:{self.__name}   Email:{self.__email}")
        print("Order Details")
        for order in self.__orders:
            print(f"Order ID:{order.getOrderId()}\nProducts")
            print("Name\t\tPrice")
            for products in order.getProducts():
                print(f"{products.getName()}\t\t{products.getPrice()}")
            print("Total=",order.calculateTotal())
                

def addProducts(n):
    prods=[]
    for i in range(n):
        name,price=input("Enter Name and Price of Product"+str(i+1)+':').split()
        prods.append(Product(name,float(price)))
    return prods

def addOrders(n):
    orders=[]
    for i in range(n):
        no=int(input("Enter no. of products for Order"+str(i+1)+':'))
        oid=int(input("Enter Order Id:"))
        orders.append(Order(oid,addProducts(no)))
    return orders

def main():
    cust=[]
    n=int(input("Enter no. of customers:"))
    for i in range(n):
        orders=[]
        name,email=input("Enter Name and Email").split()
        no=int(input("Enter no. of orders:"))
        customer=Customer(name,email)
        cust.append(customer)
        orders=addOrders(no)
        for order in orders:
            customer.placeOrders(order)
    for c in cust:
        c.display()


if __name__ == "__main__":
    main()
        

        