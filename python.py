# Write a python program to calculate area of 10 different circles. Given the pi = 22/7 and the radius of circles entered by user using simple function, parameterized function, return type with function and return type with parameterized function

def area_1(r):
    pi = 22/7
    return pi * r * r


def area_2():
    pi = 22/7
    r = int(input('Enter the radius: '))
    return pi * r * r


def area_3(r):
    pi = 22/7
    print(round((pi * r * r), 3))


def area_4():
    r = int(input('Enter the radius: '))
    pi = 22/7
    print(round((pi * r * r), 3))


for i in range(3):
    print(round(area_1(r=int(input("Enter radius: "))), 3))

for i in range(2):
    print(round(area_2(),3))

for i in range(3):
    area_3(r=int(input("Enter radius: ")))

for i in range(2):
    area_4()

#
# def simFunc(n):
#     for i in range(1, 11):
#         print("{0} X {1} = {2}".format(n, i, n*i))
#
#
# def paramFunc(n, limit):
#     for i in range(1, limit+1):
#         print("{0} X {1} = {2}".format(n, i, n*i))
#
#
# def simFuncWR(n):
#     table = []
#     for i in range(1, 11):
#         table.append(n*i)
#     return table
#
#
# def paramFuncWR(n, limit):
#     table = []
#     for i in range(1, limit+1):
#         table.append(n*i)
#     return table
#
#
# print('''
# How do you want to print multiplication table?
# Enter 1 for using simple function
# Enter 2 for using parameterized function
# Enter 3 for using return type simple function
# Enter 4 for using return type parameterized function
# ''')
#
# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#     for i in range(2, 21):
#         simFunc(i)
#         print()
#
# elif choice == 2:
#     limit = int(input("Enter the limit of the table: "))
#     for i in range(2, 21):
#         paramFunc(i, limit)
#         print()
#
# elif choice == 3:
#     for i in range(2, 21):
#         table = simFuncWR(i)
#         print("{0} Table: {1}".format(i, table))
#         print()
#
# elif choice == 4:
#     limit = int(input("Enter the limit of the table: "))
#     for i in range(2, 21):
#         table = paramFuncWR(i, limit)
#         print("{0} Table: {1}".format(i, table))
#         print()
#
# else:
#     print("Invalid choice.")