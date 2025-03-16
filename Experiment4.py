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

'''3. Print Fibonacci series up to given term.'''

num = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a = 0  # First term
b = 1  # Second term

# Check if the user entered 1 or more terms
if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print("Fibonacci series: 0")
else:
    print("Fibonacci series:")
    print(a, b, end=" ")  # Print first two terms

    # Print the remaining terms
    for _ in range(num - 2):  # Already printed first two terms
        c = a + b  # Next term is the sum of the last two terms
        print(c, end=" ")
        a = b  # Move 'b' to 'a'
        b = c  # Move 'c' to 'b'

'''4. Write a program to find if given number is prime number or not. '''

prime = int(input("Enter a number to check if it's prime: "))
if prime < 2:
    print(f"{prime} is not a prime number")
else:
    for i in range(2, prime):
        if prime % i == 0:
            print(f"{prime} is not a prime number")
            break
    else:
        print(f"{prime} is a prime number")

'''5. Check whether given number is palindrome or not. '''

num = int(input("Enter a number: "))
original_num = num  # Store the original number
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original_num == reverse:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

