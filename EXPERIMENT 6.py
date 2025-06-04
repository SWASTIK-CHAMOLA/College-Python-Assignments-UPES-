# 1. Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("Enter how many numbers you want to input: "))
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
print("Enter the numbers (only 0, 1, 2, or 3) separated by spaces:")
numbers = input().split()
for num in numbers:
    num = int(num)
    if num == 0:
        count_0 += 1
    elif num == 1:
        count_1 += 1
    elif num == 2:
        count_2 += 1
    elif num == 3:
        count_3 += 1
    else:
        print("Invalid number! Please enter only 0, 1, 2, or 3.")
print("Count of 0:", count_0)
print("Count of 1:", count_1)
print("Count of 2:", count_2)
print("Count of 3:", count_3)

# 2. Create a tuple to store n numeric values and find average of all values.

b = int(input("Enter how many numbers you want to find the average of: "))
numbers = ()
print("Enter the numbers:")
for i in range(b):
    num = int(input())
    numbers += (num,)
average = sum(numbers) / b
print("Numbers entered:", numbers)
print("Average:", average)

#   QUESTION 3
# Get the number of students
N = int(input("Enter the number of students: "))

print("Enter the scores separated by spaces:")
scores = input().split()  # Split input into separate values (as strings)

# Convert scores to integers one by one
scores_int = []
for score in scores:
    scores_int.append(int(score))

# Sort the scores in descending order
scores_int.sort(reverse=True)

# Find the highest score
highest = scores_int[0]

# Find the runner-up (second highest) score
runner_up = None
for score in scores_int:
    if score < highest:  # First number smaller than the highest
        runner_up = score
        break  # Stop searching once we find the runner-up

if runner_up is not None:
    print("Runner-up score:", runner_up)
else:
    print("No runner-up exists.")

''' 4. Create a dictionary of n persons where key is name and value is city. 
a) Display all names 
b) Display all city names 
c) Display student name and city of all students. 
d) Count number of students in each city. 
'''

# Create an empty dictionary
students = {}
# Get the number of persons
n = int(input("Enter the number of persons: "))

# Input name and city for each person
for i in range(n):
    name = input(f"Enter name of person {i+1}: ")
    city = input(f"Enter city of {name}: ")
    students[name] = city  # Add to dictionary

# a) Display all names (keys)
print("\nAll names:")
for name in students.keys():
    print(name)

# b) Display all city names (values)
print("\nAll city names:")
for city in set(students.values()):  # Using set to avoid duplicate city names
    print(city)

# c) Display student name and city
print("\nStudent name and city:")
for name, city in students.items():
    print(f"{name} - {city}")

# d) Count number of students in each city
city_count = {}
for city in students.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nNumber of students in each city:")
for city, count in city_count.items():
    print(f"{city}: {count}")


# QUESTION 5
# Create an empty dictionary to store movie details
movies = {}

# Get the number of movies
n = int(input("Enter the number of movies: "))

# Input movie details
for i in range(n):
    print(f"\nEnter details for Movie {i+1}:")
    name = input("Movie Name: ")
    year = int(input("Release Year: "))
    director = input("Director Name: ")
    production_cost = float(input("Production Cost (in crores): "))
    collection = float(input("Collection Made (in crores): "))

    # Store details in a dictionary
    movies[name] = {
        "Year": year,
        "Director": director,
        "Production Cost": production_cost,
        "Collection": collection
    }

# a) Print all movie details
print("\nAll Movie Details:")
for name, details in movies.items():
    print(f"\nMovie: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")

# b) Display name of movies released before 2015
print("\nMovies Released Before 2015:")
for name, details in movies.items():
    if details["Year"] < 2015:
        print(name)

# c) Print movies that made a profit
print("\nMovies That Made a Profit:")
for name, details in movies.items():
    if details["Collection"] > details["Production Cost"]:  # Profit condition
        print(name)

# d) Print movies directed by a particular director
search_director = input("\nEnter Director Name to search for their movies: ")
print(f"\nMovies directed by {search_director}:")
found = False
for name, details in movies.items():
    if details["Director"].lower() == search_director.lower():  # Case-insensitive match
        print(name)
        found = True
if not found:
    print("No movies found for this director.")

print('SWASTIK CHAMOLA \nBatch: 51\n SAP ID: 590016735')
