num = int(input("Enter 3-digit number : "))
sum = 0
temp = num
i=1
while i<1001:
 digit = temp % 10
 sum += digit * digit * digit
 temp = temp//10
 if sum==num:
  print('It is an Armstrong number')
 else:
  print('It is not an Armstrong number')