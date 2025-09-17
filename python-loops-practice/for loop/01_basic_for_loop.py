# Looping through a list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# Looping through range of numbers
for i in range(5):
    print(i)

# Looping through a string
for char in "PYTHON":
    print(char)

# Using for loop with else
for i in range(3):
    print(i)
else:
    print("Loop is over")

# Custom start & step in range
for i in range(2, 10, 2):
    print(i)

# Iterating with enumerate
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):  # enumerate returns index and value
    print(index, name)

# Iterating with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):  # zip combines two lists
    print(name, age)

# List comprehension
squares = [x**2 for x in range(5)]  # squares of numbers from 0 to 4
print(squares)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # even numbers
print(even_squares)

odd_squares = [x**2 for x in range(10) if x % 2 != 0]  # odd numbers
print(odd_squares)

# Dictionary iteration
person = {"name": "Tanim", "age": 30, "city": "Bangladesh"}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():
    print(key, ":", value)
