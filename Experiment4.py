                                #Experiment 4: Loops

'''1. Find a factorial of given number. '''

q = int(input("Enter the no you want to find factorial of: "))
factorial = 1
for i in range(q,1,-1):
    factorial = factorial * i
print(factorial)

