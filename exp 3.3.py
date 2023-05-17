# file= open('geek.txt')
# for each in file:
#     print(each)

#
# file=open("geek.txt")
# a=file.read()
# print(a)
# file.close()



# 1.1
# import string
# alphabet = list(string.ascii_uppercase)
# for i in alphabet:
#  file = open(f"{i}.txt",'w')
#  file.close()
# 1.2
# import string
# alphabet = list(string.ascii_uppercase)
# j = 1
# file = open("geek.txt",'a')
# for i in alphabet:
#  file.write(f'{j} = {i}\n')
#  j+=1

# 1.3

# import random
# def random_line(fname):
#     lines = open(fname).read().splitlines()
#     return random.choice(lines)
# print(random_line('geek.txt'))


# 1.4
#
# file = open("geek.txt",'r')
# counter = 0
# for i in file:
#  for word in i:
#   if word == 'A':
#    counter+=1
# print(f'A has appeared {counter} times')

# 1.5

file = open("geek.txt",'r')
file2 = open("A.txt",'a')
content = file.readlines()
for i in content:
 file2.write(i)