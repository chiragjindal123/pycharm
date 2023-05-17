# 5. Program to demonstrate polymorphism in python
# class a:
#  def intro(self):
#   print("Subhprabhat")
#  def flight(self):
#   print("Good Morning")
# class b(a):
#  def flight(self):
#   print("Good Afternoon")
# class c(a):
#  def flight(self):
#   print("Good Evening")
# obj_a = a()
# obj_b = b()
# obj_c = c()
# obj_a.intro()
# obj_a.flight()
# obj_b.intro()
# obj_b.flight()
# obj_c.intro()
# obj_c.flight()


# 1. Program to implement an object class in Python
# class Employee:
#  employee_id = 0
# employee1 = Employee()
# employee2 = Employee()
# employee1.employeeID = 10014541
# print(f"Employee ID: {employee1.employeeID}")
# employee2.employeeID = 1002684
# print(f"Employee ID: {employee2.employeeID}")

# 2.Program to implement inheritance in Python


# class Animal:
#  def breed(self):
#   print("sher")
#
#
# class cat(Animal):
#  def eat(self):
#   print("khana")
#
#
# class Child(cat):
#  def big_cat(self):
#   print("milk")
#
#
# d = Child()
# d.breed()
# d.eat()
# d.big_cat()



# 3. Program to demonstrate operator overloading in Python
# class Point:
#  def __init__(self, x=0, y=0):
#   self.x = x
#   self.y = y
#  def __str__(self):
#   return "({0},{1})".format(self.x, self.y)
#  def __add__(self, other):
#   x = self.x + other.x
#   y = self.y + other.y
#   return Point(x, y)
#
# p1 = Point(7, 8)
# p2 = Point(2, 8)
# print(p1+p2)

# 4.Program to demonstrate method overriding in Python.


class Parent():
 def __init__(self,age):
  self.value = "Parent"
  self.age = age

 def show(self):
  print(self.value)
  print(self.age)


class Child(Parent):
 def __init__(self):
  self.value = " Child"

 def show(self):
  print(self.value)


obj1 = Parent(20)
obj2 = Child()

obj1.show()
obj2.show()
