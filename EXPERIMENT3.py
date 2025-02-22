# Experiment 3 : Conditional Statements
''' 1. Check whether given number is divisible by 3 and 5 both.'''

a = int(input("enter the number: "))
if a%3==0 and a%5 == 0:
    print("No is divisible by 3 and 5",a)
else:
    print ("Not divisible by 3 and 5",a)
  
'''2. Check whether a given number is multiple of five or not. '''

a = int(input("enter the number"))
if a%5==0:
    print("No is the factor of 5")
else:
    print("No is not the factor of 5")

''' 3. Find the greatest among two numbers. If numbers are equal than print “numbers are equal”. '''

a = int(input("enter the 1st number"))
b = int(input("enter the 2nd number"))
if a>b:
    print("1st no is greater")
elif b>a:
    print("2nd no is greater")
else:
    print("they are equal")

''' 4. Find the greatest among three numbers assuming no two values are same. '''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    greatest = num1
elif num2 > num1 and num2 > num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest number is: {greatest}")
