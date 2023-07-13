'''
Create an oop that allows you to enters data for customer and employesss.
create a person class with attributes first name, last name and email. This class should have a method  that return full name.

Craete a employee class that inherits the person class , ad an attribute for customer no.

Create a customer class which inherits a person class , add an attribute pan number.

The program should create a Customer and Employee object from the data entered by the user and it should use this object to display the 
data to the user. to do that the program can use isinstance() function to check whether the object is a customer or employee
'''

class Person:
    def __init__(self, fname, lname, email):
        self.email = email
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f"{self.fname} {self.lname}"

class Employee(Person):
    def __init__(self, fname, lname, email, employee_no):
        super().__init__(fname, lname, email)
        self.employee_no = employee_no
    def display(self):
        print(f"Full name: {self.full_name()}")
        print(f"Email: {self.email}")
        print(f"Employee number: {self.employee_no}")
        print()



class Customer(Person):
    def __init__(self, fname, lname, email, pan_number):
        super().__init__(fname, lname, email)
        self.pan_number = pan_number
    def display(self):
        print(f"Full name: {self.full_name()}")
        print(f"Email: {self.email}")
        print(f"PAN number: {self.pan_number}")
        print()


def enter_data():
    people = []
    while True:
        fname = input("Enter first name (or 'q' to quit): ")
        if fname == 'q':
            break
        lname = input("Enter last name: ")
        email = input("Enter email: ")
        person_type = input("Is this a customer or an employee? (c/e): ")
        if person_type == 'c':
            pan_number = input("Enter PAN number: ")
            people.append(Customer(fname, lname, email, pan_number))
        elif person_type == 'e':
            employee_no = input("Enter employee number: ")
            people.append(Employee(fname, lname, email, employee_no))
       
        else:
            print("Invalid input")
        print()
    return people

def display_data(people):
    for person in people:
        if isinstance(person, Customer):
            print("Customer")
            person.display()
        elif isinstance(person, Employee):
            print("Employee")
            person.display()

def main():
    people = enter_data()
    display_data(people)

if __name__ == "__main__":
    main()
