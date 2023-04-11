# txt = "HELLO MY FRIENDS"
# tx = "hello my "
# form = "For only {price:.2f} dollars!"
#
# x = txt.lower()
# y = tx.upper()
# z = tx.capitalize()
# a = txt.casefold()
# b = txt.center(20)
# c = txt.count('MY')
# d = form.format(price = 49)
#
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)
# print(d)

# Q2 Write a program to count number of vowels in a string

str = "HEllo WOrld"
cnt = 0
for c in str:
    if c.lower() in ['a','e','i','o','u']:
        cnt+=1
print(cnt)

# Q3 WAP to count number of spaces in string

str = " H E L L "
cnt=0
for c in str:
    if c==" ":
        cnt+=1
print(cnt)

# Q4 WAP to count number of lines in string

str = """ Hello,
        My name is
        Chirag"""
cnt=1 # number of lines would be 1 + cnt('\n') in string
for c in str:
    if c=="\n":
        cnt+=1
print(cnt)




#1.Find Number Of Vowels In String.
#2.Convert Lower Case to Upper And Vice-Versa
#3.Find No of Lines, spaces and consider digits as blank spaces

# def countn(str):
#     cn=0;
#     for i in str:
#         if i=="\n":
#             cn=cn+1
#     return cn
#
# def isalpha(s):
#     st=ord(s)
#     print(st)
#     if(st<65 and st>90 or st<95 and st>122):
#         return 1
#     else:
#         return 0
#
# def counts(str):
#     cs=0
#     for i in str:
#         if i==" " or i in '123456789':
#             cs=cs+1
#     return cs
#
# def countv(str):
#     cv=0
#     for i in str:
#         if i in 'aeiouAEIOU':
#             cv+=1
#     return cv
#
# def conv(str):
#     s=""
#     for i in str:
#         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             s=s+chr(ord(i)+32)
#         elif i in 'abcdefghijklmnopqrstuvwxyz':
#             s=s+chr(ord(i)-32)
#         else:
#             s=s+i
#     return s
#
# str="""Python
#  is
#     very cool123"""
# newlines=countn(str)
# space=counts(str)
# vowel=countv(str)
# nstr=conv(str)
# print("Spaces:",space,"\nNewlines:",newlines,"\nVowels:",vowel,"\nString After Conversion is:"+nstr)
#








