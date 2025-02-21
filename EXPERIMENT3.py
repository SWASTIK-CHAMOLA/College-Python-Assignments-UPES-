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
