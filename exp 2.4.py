# 1.	Write a Python program to replace last value of tuples in a list
tuple1 = (1,2,3,4,5,6,7)
list1 = list(tuple1)
list1[5] = 9
tuple1 = tuple(list1)
print(tuple1)

# 2.	Write a Python program to remove an empty tuple(s) from a list of tuples
tuple1 = ((1, 2), (), (3, 4), (), (5,))
list1 = list(tuple1)
for i in list1:
    if i==():
        list1.remove(i)
print(list1)

# 3.Write a Python program calculate the product, multiplying all the numbers of a given tuple.

tup = (2,1,4,6,7)
product = 1
for i in tup:
    product = product*i
print(product)

# d)	Write a Python program to convert a tuple of string values to a tuple of integer values


tup = ('2','7','14','21','28','35')
listy = []
for i in tup:
    listy.append(int(i))
tup2 = tuple(listy)
print(tup2)

# 5.	Write a Python program to check if a specified element presents in a tuple of tuples

tup = ((1,2,3),('apple','orange'),('tgif','aa','vvv'))
def search(tup,element):
    flag=0
    a=0
    for i in tup:
        b=0
        for j in i:
            if(j==element):
                return True, a, b
            b+=1
        a+=1
    return False
print(search(tup,'tgif'))


