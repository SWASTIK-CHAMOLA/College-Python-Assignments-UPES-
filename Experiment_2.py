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
