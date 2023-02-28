#Python program to check if a given number is palindrome or not

# lower_word=input()
#
# reverse_word = ""
#
# for i in lower_word:
#     reverse_word=i+reverse_word
#
# if reverse_word==lower_word:
#   print("palindrome")
#
# else:
#   print("not a palindrome")

#given number is palindrome or not
# num = 1221
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if num == reverse:
#   print('Palindrome')
# else:
#   print("Not Palindrome")

#Python program to check if given number is armstrong or not
#
n=153
temp=n
sum=0
while n>0:
    r=n%10
    sum+=r*r*r
    n//=10


if sum==temp:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")


#Python program to find the greatest of 3 numbers
#
# a=int(input())
# b=int(input())
# c=int(input())
#
# if (a>=b) and (a>=c):
#     print("the greatest number is :" ,a)
#
# elif (b>=c) and (b>=c):
#     print("the greatest number is :" ,b)
#
# else:
#     print("the greatest number is : ",c)