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

''' 5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots. '''

a = int(input("enter a value "))
b = int(input("enter b value "))
c = int(input("enter c value "))
print(f"b value {b} a value {a} c value {c}")
k =  b**2 -  4*a*c
if k >= 0: 
    k = k ** 0.5 
    x1 = (-b + k) / (2 * a)
    x2 = (-b - k) / (2 * a)
    print(f"The roots are real and are: {x1} and {x2}")
else:  
    real_part = -b / (2 * a)
    imaginary_part = (-k) ** 0.5 / (2 * a)

'''6. Find whether a given year is a leap year or not.'''
def leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
print(leap(year))
