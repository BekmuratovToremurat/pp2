#Python also has a function that will make the child class inherit all the methods and properties from its parent:super()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
#Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

