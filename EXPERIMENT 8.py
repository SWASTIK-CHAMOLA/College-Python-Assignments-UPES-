''' 1. Add few names, one name in each row, in “name.txt file”. a. Count no of names b. Count all names starting with vowel c. Find longest name. '''
# Creating name.txt with names
with open("name.txt", "w") as f:
    f.write("Ananya\n")
    f.write("Rahu1\n")
    f.write("Isha\n")
    f.write("On\n")
    f.write("Esha\n")
    f.write("Suresh\n")

# Count number of names and analyze
with open("name.txt", "r") as f:
    names = [line.strip() for line in f]

count_names = len(names)
vowel_names = [name for name in names if name[0].lower() in 'aeiou']  # Fixed typo ('aelou' → 'aeiou')
longest_name = max(names, key=len)

print("Number of names:", count_names)
print("Names starting with a vowel:", len(vowel_names))  # Added 'a' for grammar
print("Longest name:", longest_name)
print('SWASTIK CHAMOLA \nBatch: 51\nSAP ID: 590016735')  # Fixed typo ('SMASTIK CHAWOLA')

''' 2. Processing Integers from a File. '''
# Create integer.txt and write numbers
with open("integer.txt", "w") as f:
    f.write("34\n120\n99\n205\n88\n300\n")

# Read and process numbers
with open("integer.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

max_num = max(nums)
avg = sum(nums) / len(nums)
greater_than_100 = len([n for n in nums if n > 100])

print("Maximum number:", max_num)
print("Average:", avg)
print("Count > 100:", greater_than_100)

''' 3. Processing city.txt File. '''
# Creating city.txt
with open("city.txt", "w") as f:
    f.write("Dehradun 5.78 308.20\n")
    f.write("Delhi 190 1484\n")
    f.write("Mumbai 204 603\n")
    f.write("Bangalore 84 741\n")
    f.write("Ranchi 11 652\n")

# Processing city file
with open("city.txt", "r") as f:
    cities = [line.strip().split() for line in f]

print("City Details:")
for city in cities:
    print(f"{city[0]:<10} | Population: {city[1]:>6} lakhs | Area: {city[2]:>7} km²")

print("\nCities with population > 10 Lakhs:")
for city in cities:
    if float(city[1]) > 10:
        print(city[0])

total_area = sum(float(city[2]) for city in cities)
print(f"\nSum of areas: {total_area} km²")

''' 4. Integer Division with Exception Handling. '''
# Sample input simulation
test_cases = ["1 0", "2 5", "3 1", "4 x", "5 2"]

print("Division Results:")
for line in test_cases:
    try:
        a, b = map(int, line.split())
        print(f"{a} // {b} = {a // b}")
    except ZeroDivisionError as e:
        print(f"Error Code: integer division by zero (input: '{line}')")
    except ValueError as e:
        print(f"Error Code: invalid literal for int() (input: '{line}')")

''' 5. Custom Exception Handling in File Operations. '''

class FileOpenError(Exception):
    pass

class FileEmptyError(Exception):
    pass

try:
    filename = "data.txt"
    try:
        with open(filename, "r") as f:
            data = f.read()
            if not data.strip():
                raise FileEmptyError("The file is empty.")
        print("File read successfully!")
    except FileNotFoundError:
        raise FileOpenError(f"File '{filename}' not found.")

except FileOpenError as e:
    print(f"Custom Error (File Access): {e}")
except FileEmptyError as e:
    print(f"Custom Error (Content Issue): {e}")
