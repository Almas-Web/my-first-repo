# create a set 
#empty set
s = set()
print(s)
print(type(s))

# with elements
fruits = {"apple", "banana", "mango", "orange"}
print(fruits) # order not maintained /fixed

# duplicate values are automatically removed
fruits = {"apple", "banana", "mango","mango", "orange", "apple","apple", "banana"}
print(fruits) # order not maintained /fixed

# add elements

fruits= {"apple", "banana", "mango", "orange"}
fruits.add("grape")
print(fruits)

# remove elements
fruits= {"apple", "banana", "mango", "orange"}
fruits.remove("banana")
print(fruits)
#fruits.remove("grape") # will show error if the element is not found
#print(fruits)
fruits.discard("grape") # will not show error if the element is not found
print(fruits)

removed_item=fruits.pop()
print("Removed item:", removed_item)
print(fruits)
fruits.clear()
print(fruits)

# converts set to list
fruits= {"apple", "banana", "mango", "orange"}
fruits_list=list(fruits)
print(fruits_list)
print(type(fruits_list))

#converts set to tuple
fruits= {"apple", "banana", "mango", "orange"}
fruits_tuple=tuple(fruits)
print(fruits_tuple)
print(type(fruits_tuple))