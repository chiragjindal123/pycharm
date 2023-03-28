# def last(n):
#      return n[-1]
#
#
# def sort(a):
#      return sorted(a, key=last)
#
#
# a = [(1, 2, 3), (3, 3, 4), (2, 1, 8)]
# print("Sorted:")
# print(sort(a))

# from operator import itemgetter as i
# a = [(1, 2, 3), (3, 3, 4), (2, 1, 8)]
# a.sort(key=i(2))
# print (a)


a = ['a', 'b', 'c', 'd', 'e', 'f']
del a[5], a[4], a[0]
print (a)

