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

'''7. Write a program which takes any date as input and display next date of the 
calendar 
e.g. 
I/P: day=20 month=9 year=2005  
O/P: day=21 month=9 year 2005 '''
b = input("Enter the month: ").lower()
a = int(input("Enter the day of the month: "))
c = int(input("Enter the year: "))
months_31 = ('january', 'march', 'may', 'july', 'august', 'october', 'december')
months_30 = ('april', 'june', 'september', 'november')
a += 1  
if b in months_31:
    if a > 31:
        a = 1
        if b == 'december':  
            b = 'january'
            c += 1  
elif b in months_30:
    if a > 30:
        a = 1
elif b == 'february':
    leap_year = (c % 4 == 0 and c % 100 != 0) or (c % 400 == 0)
    if leap_year:
        max_days = 29
    else:
        max_days = 28

    while a > max_days:
        print("Invalid input for February")
        break
    
    if a > max_days:  
        a = 1
        b = 'march'
if b == 'december' and a == 1:
    print(f"year: {c}")

print("Next day:", a)
print(f"year is {c}")
print(f"month is {b}")

'''
8. Print the grade sheet of a student for the given range of cgpa. Scan marks of 
five subjects and calculate the percentage. 
CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A 
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding) 
 
 
80  
 
Sample Gradesheet 
Name: Rohit Sharma 
Roll Number: R17234512   SAPID: 50005673 
Sem: 1      Course: B.Tech. CSE AI&ML 
 
Subject name: Marks 
PDS:   70 
Python:  80 
Chemistry:  90 
English:  60 
Physics:  50 
Percentage: 70% 
CGPA:7.0 
Grade:   '''

name = input("Enter your name: ")
k = int(input("Enter your Physics marks: "))
l = int(input("Enter your Python marks: "))
m = int(input("Enter your Chemistry marks: "))
n = int(input("Enter your English marks: "))
o = int(input("Enter your PDS marks: "))
per= (k+l+m+n+o)/500
per = per*100
print("\n")

print("Name: ",name,"\nRoll no: 13238482","\nSemester 1","\nSAP-ID: 44292948","\nCourse: Btech CSE")
print("\n")
print("Physics:", k, "\nPython:", l, "\nChemistry:", m, "\nEnglish:", n, "\nPDS:", o)
print("percentage: ",per)
c=per/10
print("CGPA is: ",c)

if c == 0 or c <= 3.4:
    print("Grade is F")
elif c == 3.5 or c <= 5:
    print("Grade is C+")
elif c == 5.1 or c <= 6:
    print("Grade is B")
elif c == 6.1 or c <= 7:
    print("Grade is B+")
elif c == 7.1 or c <= 8:
    print("Grade is A")
elif c == 8.1 or c <= 9:
    print("Grade is A+")
elif c == 9.1 or c <= 10:
    print("Grade is O(outstanding)")
