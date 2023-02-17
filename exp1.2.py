#Python program to check if a given number is palindrome or not

lower_word=input()

reverse_word = ""

for i in lower_word:
    reverse_word=i+reverse_word

if reverse_word==lower_word:
  print("palindrome")

else:
  print("not a palindrome")

#Python program to check if given number is armstrong or not

n=153
temp=n
sum=0
while n>0:
    r=n%10
    sum+=r*r*r
    n/=10
    n=int(n)

if int(sum)==temp:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")


#Python program to find the greatest of 3 numbers

a=int(input())
b=int(input())
c=int(input())

if (a>=b) and (a>=c):
    print("the greatest number is :" +str(a))

elif (b>=c) and (b>=c):
    print("the greatest number is :" +str(b))

else:
    print("the greatest number is : " +str(c))