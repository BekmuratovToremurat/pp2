#When you add the function, the child class will no longer inherit the parent's function.__init__()__init__()
#Note: The child's function overrides the inheritance of the parent's function.__init__() __init__()
#To keep the inheritance of the parent's function, add a call to the parent's function:__init__()__init__()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()