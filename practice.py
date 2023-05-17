# # def area(r):
# #     pie=22/7
# #     ar=pie*r*r
# #     print("area = %.2f"%ar)
# #     return ar
# # i=0
# # for i in range(2):
# #     a=int(input("enter radius:"))
# #     area(a)
# #
# #
# #
# # lst = []
# # n = int(input("Enter number of elements : "))
# # for i in range(0, n):
# #     ele = int(input())
# #
# #     lst.append(ele)
# #
# # print(lst)
# # x = max(lst)
# #
# # print(x)
#
#
#
# class Employee:
#  employee_id = 0
# employee1 = Employee()
# employee2 = Employee()
# employee1.employee_id = 10014541
# print(f"Employee ID: {employee1.employee_id}")
# employee2.employee_id = 1002684
# print(f"Employee ID: {employee2.employee_id}")



class Point:
 def __init__(self, x=0, y=0):
  self.x = x
  self.y = y
 def __str__(self):
  return "({0},{1})".format(self.x, self.y)
 def __add__(self, other):
  x = self.x + other.x
  y = self.y + other.y
  return Point(x, y)

p1 = Point(7, 8)
p2 = Point(2, 8)
print(p1+p2)
