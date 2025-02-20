# EXPERIMENT-1: Python Installation and starting with python
'''
 2. Write Python programs to print strings in the given manner: 
a)   Hello Everyone !!! 
b)   Hello 
      World 
c)   Hello 
              World 
d) ‘ Rohit’ s date of birth is 12\05\1999’ 
'''
print("\nSWASTIK CHAMOLA\nBATCH - 51\nSAP ID: 590016735\n")
print("HELLO EVERYONE !!")
print("HELLO\nWORLD ")
print("HELLO\n        WORLD ")
print("Rohit’ s date of birth is 12\05\1999")

'''3  Declare a string variable called x and assign it the value “Hello”. 
            Print out the value of x '''
x ="Hello"
print(x)
'''
 4 Take different data types and print values using print function. 
'''
x = 10
y = -10
a = 10.5
b = -10.5
A="swastik"
B="chamola"
print(a)
print(b)
print(A)
print(B)
print(x)
print(y)
print(type(a))  
print(type(b))
print(type(x))
print(type(y))

'''  5 Take two variable a and b. Assign your first name and last name. Print your Name 
after adding your First name and Last name together. '''
f = "SWASTIK"
l = "CHAMOLA"
print(f,"",l )

'''  6   Declare three variables, consisting of your first name, your last name and Nickname.
Write a  program that prints out your first name, then your nickname in parenthesis and then your last name.   
Example output : George ( woody ) Washington. '''
g = input("enter your first name")
m = input("enter your nickname")
gm = input("enter your last name")
print(g , " (" , m , ") " , gm)

'''  7 Declare and assign values to suitable variables and print in the following way : 
NAME : NIKUNJ BANSAL   
SAP ID : 500069944 
DATE OF BIRTH : 13 Oct 1999 
ADDRESS : UPES 
                    Bidholi Campus 
                    Pincode : 248007 
Programme : AI & ML                                                                                       
Semester : 2 '''
q = input("enter your name")
print("NAME : ",q)
B = int(input("enter your SAP ID: "))
print("SAP ID: : ",B)
Q = input("enter your D.O.B")
print("D.O.B : ",Q)
address = [
    "ADDRESS : UPES",
    "Bidholi Campus",
    "Pincode : 248007",
    "Programme : AI & ML",
    "Semester : 2"
]

for i in address:
    print(i)
