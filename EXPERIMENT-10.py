# 1. Create NumPy Array and Find Sum of All Elements
arr = np.array([1, 2, 3, 4, 5])
total = np.sum(arr)
print("Array:", arr)
print("Sum of all elements:", total)

# 2. Create (3x3) NumPy Array and Perform Row/Column-wise Sum and Find 2nd Maximum Element
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)
second_max = np.sort(arr.flatten())[-2]

print("Array:\n", arr)
print("Row-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)
print("Second Maximum Element:", second_max)

# 3. Perform Matrix Multiplication of Two n x n Matrices
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Multiplication Result:\n", result)

# 4. Pandas Program to Raise Array Elements to Powers of Another Array (Element-wise)
import pandas as pd
df = pd.DataFrame({
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
})

result = df['X'] ** df['Y']
print("First few values of result (X^Y):")
print(result.head())

# 5. Get First 3 Rows of a Given DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index=labels)
print("First three rows of the data frame:")
print(df.head(3))

# 6. Replace Missing Values in DataFrame
import numpy as np
import pandas as pd

# Define data and labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

df['score'].fillna(0, inplace=True)

print("DataFrame after replacing NaN in 'score' column with 0:")
print(df)

# 7. Demonstrate Visual Forms Using Matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

# Line Chart
plt.figure(figsize=(6,4))
plt.plot(x, y, label='Line Chart')
plt.title("Line Graph Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

