a = {1:'ram',2:'rahul',3:'prince'}
print(a)

print(len(a))

x=a.keys()
print(x)

y=a.get(2)
print(y)

a.update({4:'chirag'})
print(a)
print(a.values())


c=a.copy()
print(c)


del a[1]
print(a)

q=a.clear()
print(q)
