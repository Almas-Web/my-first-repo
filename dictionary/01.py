# empty dictionary 
my_dict = {}
print(my_dict) 
print(type(my_dict))  

# dictionary with values 

student ={
    "name": "Almas",
    "age": 23,
    "is_student": True
    
    }
print(student)

# Acceessing values in dictionary

student ={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

}
#Approach 1  (bracket notation)
# syntax: dictionary_name[key]
print(student["name"])
print(student["age"])
print(student["Roll"])
print(student["University"])

#Approach 2 (get method)
# syntax: dictionary_name.get(key)
print(student.get("name"))
print(student.get("age"))
print(student.get("Roll"))
print(student.get("University"))

#Adding and updating new value 
student ={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

}
student["age"]=24 #updating existing value
student["is_student"]=True #adding new key-value pair
print(student)

student.get("age") ==25 #updating existing value  don't forget == for comparison
student.get("is_student")==False #adding new key-value pair
print(student)

# Removing  items from dictionary
student ={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

}
#Approach 1 (pop method)
student.pop("Roll")
print(student)
#Approach 2 (del keyword)
del student["University"]  
print(student)
#Approach 3 (clear method)
student.clear()
print(student)

#Looping through a dictionary
student ={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

}
for key in student :
    print("key:",key)
for value in student.values():
    print("value:",value)
for key,value in student.items():
    print(key,":",value)

# Nested dictionary
students = {
    "student1": {"name": "Alice", "age": 21},
    "student2": {"name": "Bob", "age": 22}
}
#approach 1 (bracket notation)
print(students["student1"]["name"])  
print(students["student2"]["age"])   

#approach 2 (.get method)
print(students.get("student1").get("name"))
print(students.get("student1").get("age"))
print(students.get("student2").get("name"))
print(students.get("student2").get("age"))

# using the dic() constructor
book=dict(title="1984", author="A",published="1949")

print(book)