class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # Invoking the __init__ of the parent class


    def display(self):
        print ("Name:", self.name)
        print("Salary:", self.salary)
        print("Post:", self.post)

# Creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# Calling the modified display function of the class Employee
a.display()