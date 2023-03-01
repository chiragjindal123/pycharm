#arthemetic operations
print("enter the first value")
a=float(input())
print("enter the second value")
b=float(input())

c=a+b
d=a-b
e=a*b
f=a/b
g=a%b

print('addition =',c,'\nsubstraction =',d,'\nmultiplication =',e,'\ndivision',f,'\nreminder',g)


# average and percentage of five subject
a=0
print("Enter the marks of five subjects")
for i in range (5):
    a+=int(input())
print('Total marks=',a,'\naverage marks =',a/5,'\npercentage =',a/5,"%")


#convertion

print("enter your value in centimeter")
a=float(input())

b=a*100
c=b*1000
print('In meters',b,'cm','\nIn kilometers',c,'cm;')