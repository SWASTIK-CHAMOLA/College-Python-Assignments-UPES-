'''1. Write a Python function to find the maximum and minimum numbers from a sequence (without built-in functions)'''
def find_max_min(seq):
    max_val = seq[0]
    min_val = seq[0]
    for num in seq[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# Example usage:
seq = [10, 6, 8, 90, 12, 56]
result = find_max_min(seq)
print(result)

''' 2. Write a Python function that returns the sum of cubes of all positive integers less than a given number. '''
def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

# Example usage:
print(sum_of_cubes(5))  # Output should be 100

''' 3. Write a Python function to print numbers from 1 to n using recursion (no loops). '''
def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current, end=' ')
    print_1_to_n(n, current + 1)

# Example usage:
print_1_to_n(5)

''' 4. Write a recursive function to print the Fibonacci series up to n terms. '''
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Example usage:
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]

''' 5. Write a lambda function to find the volume of a cone. '''
# Volume = (1/3) * π * r^2 * h
volume_cone = lambda r, h: (1/3) * 3.1416 * r**2 * h

# Example usage:
print(volume_cone(3, 5))  # Output: ~47.124

''' Write a lambda function which gives a tuple of max and min from a list. '''
# Using built-ins as lambda can't implement full custom logic easily otherwise
find_max_min_lambda = lambda lst: (max(lst), min(lst))

# Example usage:
print(find_max_min_lambda([10, 6, 8, 90, 12, 56]))  # Output: (90, 6)
print('SWASTIK CHAMOLA \nBatch: 51\n SAP ID: 590016735')

''' 7. Write functions to explain the following concepts: '''
def greet(name, message):
    return f"Hello {name}, {message}"

# Example usage:
print(greet(name="Swastik", message="welcome to Python"))

def greet(name="Guest"):
    return f"Hello, {name}"

# Example usage:
print(greet())           # Output: Hello, Guest
print(greet("Swastik"))  # Output: Hello, Swastik

def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example usage:
print(add_all(1, 2, 3, 4, 5))  # Output: 15

