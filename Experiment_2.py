# Experiment 2: Use of input statements, operators
'''
1. Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign 
a value of 7 to y, perform addition, multiplication, division and subtraction on 
these two variables and Print out the result.
'''

x = 9
y = 7
z=0

print("x + y", x + y)
print("x * y", x * y)
print("x / y", x / y)  # For float division
print("x - y", x - y)

''' 2. Write a Program where the radius is taken as input to compute the area of a  circle.'''
a = int(input("Enter the radius of the circle: "))
b = 3.14 * a**2
print(f"The area of the circle is: {b}")

''' 3. Write a Python program to solve (x+y)*(x+y) 
Test data : x = 4 , y = 3 
Expected output: 49 '''
x = int(input("enter value of x: "))
y = int(input("enter value of y: "))
print("output: ",{(x+y)*(x+y)})

''' 4. Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.'''

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = (a**2 + b**2)**0.5
print("The length of the hypotenuse is: ",c)

''' 5. Write a program to find simple interest. '''
#program to find simple interest
p = float(input("enter principle"))
r = float(input("enter rate"))
t = float(input("enter time"))
si = p*r*t/100
print("simple intrest is: ",si)

''' 6. Write a program to find area of triangle when length of sides are given. '''

a = float(input("Enter the length of base"))
b = float(input("Enter the length of height"))
area = 0.5*(a*b)
print("area is: ",area)

''' 7. Write a program to convert given seconds into hours, minutes and remaining seconds.'''

a = int(input("Enter time in seconds: "))
hour = a // 3600 
remaining_seconds = a % 3600  
minute = remaining_seconds // 60
second = remaining_seconds % 60  

print(f"The time is {hour} hours, {minute} minutes, and {second} seconds")

''' 8. Write a program to swap two numbers without taking additional variable.'''

a=int(input("enter 1st no: "))
b =  int(input("enter 2nd no: "))
a,b = b,a
print(f"swapped nos are {a},{b}")

'''9. Write a program to find sum of first n natural numbers. '''

n = int(input("Enter a positive integer: "))
if n < 1:
    print("Please enter a positive integer greater than 0.")
else:    
    total = n * (n + 1) // 2  
    print(f"The sum of the first {n} natural numbers is: {total}")

'''10. Write a program to print truth table for bitwise operators( & , | and ^ operators)'''

a = int(input("enter 1 or 0"))
b = int(input("enter 1 or 0"))
print("and operator: ",a&b)
print("or operator: ",a|b)
print("xor operator: ",a^b)

'''11. Write a program to find left shift and right shift values of a given number. '''

a = int(input("Enter a number to left and right shift: "))
b = int(input("Enter the number of bits to shift: "))

n = a >> b 
k = a << b  
print("Right shift result:", n)
print("Left shift result:", k)

'''12. Using membership operator find whether a given number is in sequence  (10,20,56,78,89) '''

a = (10, 20, 56, 78, 89)
print(a)
num = int(input("Enter a number to check if it's in the sequence: "))
if num in a:
    print("numis in the sequence",num)
else:
    print("num is not in the sequence",num)

''' 13. Using membership operator find whether a given character is in a string.'''

a = input("enter the string")
i = input("find character: ")
if i in a:
    print("i is in sequence: ",i)
else:
    print("not in sequence")
    
