# creating and accessing List
fruits=["Mango","Banana","Orange","Grapes","Apple"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])   # accessing last element
print(fruits[-2])   # accessing second last element

#list slicing

nums=[10,20,30,40,50,60,70,80,90,100]
print(nums)
print(nums[0:5])  #slicing first five elements
print(nums[0:10]) #slicing last five elements
print(nums[1:6]) #slicing last five elements
print(nums[5:])  #slicing from index 5 to last
print(nums[:5])  #slicing from starting to index 5
print(nums[:])   #slicing all elements
print(nums[::2]) #slicing with step 2
print(nums[::3]) #slicing with step 3
print(nums[-3:]) #slicing last three elements
print(nums[:-3]) #slicing all elements except last three elements
print(nums[::-1]) #reversing a list

#modifying list elements 
colors=["Red","Green","Blue","White","Black"]
print(colors)
colors[0]="Yellow"
print(colors)

# adding elements to a list
numbers=[10,20,30,40,50]
print(numbers)
numbers.append(60)  # adding element at the end
numbers.insert(0,5) # adding element at the beginning
numbers.extend([70,80,90]) # adding multiple elements at the end
print(numbers)

# removing elements from a list
nums=[10,20,30,40,50,60,70,80,90,100]
print(nums)
nums.remove(50)  # removing element by value
nums.pop()      # removing last element
nums.pop(0)     # removing element by index
nums.clear()    # removing all elements
print(nums)

# searching elements in a list
fruits=["Mango","Banana","Orange","Grapes","Apple","Mango"]
print("banana" in fruits)  # checking if element exists
print("Banana" in fruits)  # checking if element exists
print(fruits.index("Orange")) # getting index of an element
print(fruits.count("Apple"))  # counting occurrences of an element
print(fruits.count("Mango"))  # counting occurrences of an element

#sorting and reversing a list
nums=[50,20,70,10,90,30,80,40,60]
print(nums)
nums.sort()  # sorting in ascending order
print(nums)
nums.sort(reverse=True) # sorting in descending order
print(nums)
nums.reverse() # reversing the list
print(nums)

# looping through a list
colors=["Red","Green","Blue","White","Black"]
for color in colors:
    print(color)

# Nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])  # accessing first row
print(matrix[0][2]) # accessing element at first row and third column
print(matrix[1][1]) # accessing element at second row and second column
print(matrix[2][0]) # accessing element at third row and first column

# list comprehension
squares=[x**2 for x in range(1,11)]
print(squares)