class Product():
    def __init__(self,name,price,discountpercent):
        self.name = name
        self.price = price
        self.discountpercent = discountpercent
    def getDiscountAmount(self):
        return self.price * self.discountpercent
    def getDiscountPrice(self):
        return self.price-self.price * self.discountpercent
    def getDescription(self):
        pass

class Book(Product):
    def __init__(self,name,price,discount,author):
        super().__init__(self,name,price,discount)
        self.author = author
    def getDescription(self):
        print("Book Class")

class Movie(Product):
    def __init__(self,name,price,discount,year):
        super().__init__(self,name,price,discount)
        self.year = year
    def getDescription(self):
        print("Movie class")

