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

# list iteration with break
names = ["Alice", "Bob", "Charlie", "David", "Eve",
          "Frank", "Grace", "Heidi", "Ivan", "Judy"]
for name in names:
    if name =="David":
        print("Found!")
        break
    else:
        print("Not Found!")
# list iteration with continue
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
for fruit in fruits:
    if fruit == "apple":
        continue # skip the rest of the loop for this iteration
    print(fruit)
# using continue to find even numbers

start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
for i in range(start,end+1):
    if i%2==1:
        continue # skip the rest of the loop for this iteration
    print(i)

#using continuew to find odd numbers
start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
for i in range(start,end+1):
    if i%2==0:
        continue # skip the rest of the loop for this iteration
    print(i)

#naive way to find even numbers
start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
count=0
for i in range(start,end):
    if i%2==0:
        print(i)
        count+=1
print(f"Total even numbers between {start} and {end} is: {count}")

#naive way to find odd numbers
start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
count=0
for i in range(start,end):
    if i%2==1:
        print(i)
        count+=1
print(f"Total odd numbers between {start} and {end} is: {count}")