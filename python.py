


def simFunc(n):
    for i in range(1, 11):
        print("{0} X {1} = {2}".format(n, i, n*i))


def paramFunc(n, limit):
    for i in range(1, limit+1):
        print("{0} X {1} = {2}".format(n, i, n*i))


def simFuncWR(n):
    table = []
    for i in range(1, 11):
        table.append(n*i)
    return table


def paramFuncWR(n, limit):
    table = []
    for i in range(1, limit+1):
        table.append(n*i)
    return table


print('''
How do you want to print multiplication table?
Enter 1 for using simple function
Enter 2 for using parameterized function
Enter 3 for using return type simple function
Enter 4 for using return type parameterized function
''')

choice = int(input("Enter your choice: "))

if choice == 1:
    for i in range(2, 21):
        simFunc(i)
        print()

elif choice == 2:
    limit = int(input("Enter the limit of the table: "))
    for i in range(2, 21):
        paramFunc(i, limit)
        print()

elif choice == 3:
    for i in range(2, 21):
        table = simFuncWR(i)
        print("{0} Table: {1}".format(i, table))
        print()

elif choice == 4:
    limit = int(input("Enter the limit of the table: "))
    for i in range(2, 21):
        table = paramFuncWR(i, limit)
        print("{0} Table: {1}".format(i, table))
        print()

else:
    print("Invalid choice.")