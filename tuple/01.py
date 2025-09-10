# single element tuple
single_element_tuple = (5,) # don"t forget the comma 
print(type(single_element_tuple))  

# tuple slicing and indexing 
t=(10,20,30,40,50,60)
print(t[0]) 
print(t[1])  
print(t[-1])
print(t[-2])
print(t[1:4])
print(t[2:])
print(t[:4])

#concatenation and repetition
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)  # concatenation
print(t1*3)   # repetition
print(t2*2)   # repetition
print(t1+t2*2) # concatenation and repetition of t2
print((t1+t2)*2) # concatenation and repetition of both

# Membership testing
t=(10,20,30,40,50)
print(20 in t)  # True
print(100 in t) # False
print(60 not in t)

# tuple methods
t=(5,10,15,20,25,30,35,40,45,50,55,60)
print(t.count(15))  # count method
print(t.index(25))  # index method

# tuple unpacking

person = ("Almas", 23, "Bangladesh", "almas@gmail.com")
name,age,country,email =person  # every element should be assigned to a variable
print(name)
print(country)
print(age)
print(email)   
print(f"My name is {name}. My age is {age}. I live in {country}. My email is {email}.")

#Nested tuple 
nested=(("a",1),("b",2),("c",3),("d",4))
for key,value in nested:
    print(f"key: {key}, value: {value}")

# tuple inside a list
people=[
    ("Almas",23,"Bangladesh"),
    ("Tuba",22,"India"),
    ("Tanim",21,"Pakistan")

]
for name ,age,country in people:
    print(f"My name is {name}.My age is {age}.")
    print(f"{name} lives in {country}.")

#list in tuple
t=(1,2,[3,4,5])
t[2][0]=30
t[2][1]=40
print(t)
