# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)



# class Student(Person):
#   def __init__(self, fname, lname, id):
#     super().__init__(fname, lname)
#     self.id = 33

#   def announce_decorator(f):
#     def wrapper(self):
#         print("function about to start")
#         f(self)
#         print("ending function")
#     return wrapper
  
#   @announce_decorator
#   def printname(self):
#     Person.printname(self)
#     print(self.id)
    

# x = Student("Mike", "Olsen", 22)
# x.printname()


a = []

for i in range(20):
    a.append(i)
for i in a :
    print(i)


print()
a.sort(key=lambda x: x%7)

for i in a :
    print(i)