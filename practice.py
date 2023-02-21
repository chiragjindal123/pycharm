# def area(r):
#     pie=22/7
#     ar=pie*r*r
#     print("area = %.2f"%ar)
#     return ar
# i=0
# for i in range(10):
#     a=int(input("enter radius:"))
#     area(a)


#
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)
x = max(lst)

print(x)