# list unpacking 

persons=["almas",23,"Bangladesh"]
name,age,country=persons
print("name:",name) # don't forget the comma
print("country:",country)
print(f"My name is {name}. My age is {age}. I live in {country}.")
print("............")

# list inside a list unpacking
person=[
    ["Almas",23,"Bangladesh"]
]
name,age,county = person[0] # don't forget the index [0]
print("name:",name)
print("age:",age)
print("country:" ,county)
print(f"My name is {name}. My age is {age}. I live in {county}.")
print("............")

persons=[
    ["Almas",23],
    ["Tuba",22],
    ["Tanim",21]
]
for name,age in persons:
    print(f"My name is {name}. My age is {age}.")
print("............")

data = [1, 2, 3, 4, 5]

a, *b = data
print("a =", a)     # 1
print("b =", b)     # [2, 3, 4, 5]

*a, b = data
print("a =", a)     # [1, 2, 3, 4]
print("b =", b)     # 5

a, b, *c = data
print("a =", a)     # 1
print("b =", b)     # 2
print("c =", c)     # [3, 4, 5]

    