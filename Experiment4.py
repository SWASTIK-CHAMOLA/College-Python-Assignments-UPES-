                                #Experiment 4: Loops

'''1. Find a factorial of given number. '''

q = int(input("Enter the no you want to find factorial of: "))
factorial = 1
for i in range(q,1,-1):
    factorial = factorial * i
print(factorial)

'''2. Find whether the given number is Armstrong number. '''
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
while temp > 0:  
    digit = temp % 10  
    sum += digit ** len(str(num))  
    temp //= 10  
print(f"{num} is an Armstrong number." if num == sum else f"{num} is not an Armstrong number.")

'''2. Find whether the given number is Armstrong number.'''

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
while temp > 0:  
    digit = temp % 10  
    sum += digit ** len(str(num))  
    temp //= 10  

print(f"{num} is an Armstrong number." if num == sum else f"{num} is not an Armstrong number.")
