user_name="Almas"
user_age=23
user_country="Bangladesh"
print(f"My name is {user_name}.My age is {user_age} years old .I live in {user_country}")
print(f"My name is {user_name}.My age is {user_age} years old .I live in" +" "+ user_country )
print(f"""
      My name is {user_name}.
      My age is {user_age} years old.
      I live in {user_country}
      """  )
print(f"My name is {user_name}.\nMy age is {user_age} years old.\nI live in {user_country}")

#format method
print("My name is {}.\nMy age is {}.\nI live in {}".format(user_name,user_age,user_country))
#format method with index

print("My name is {0}.\nMy age is {1}.\nI live in {2}".format(user_name,user_age,user_country))


# type function
n1=10 
n2=3.14366
n3="Almas"
print(type(n1))
print(type(n2))
print(type(n3))
print(f"{n1} is of type {type(n1)}")

# data type string
user_name="Almas"
letter_a="A"
another_letter_a="10"
print(type(user_name))
print(type(letter_a))
print(type(another_letter_a))
print(f"{user_name} is of type {type(user_name)}")
print(f"{letter_a} is of type {type(letter_a)}")

# escape sign ---> \
# My name is "Almas"

print("My name is \"Almas\"")
print("My name is \"Almas\\\"")
print("My name is \"Almas\\\\ \"")

# use double quatation in single quatation
print('My name is "Almas"')
#use single quatation in double quatation
print("My name is 'almaws'")
# but use  double quatation in double quatation showing error 
#print("My name is "Almas"")
# but use  single quatation in single quatation showing error
#print('My name is 'Almas'')


#\n ---> new line , \t ---> tab space
print("My name is Almas.\nI live in Bangladesh")
print("My name is Almas.\tI live in Bangladesh")
print("My name is Almas.\n\tI live in Bangladesh") 


# print(type("10") type(10))
print(f"{type('10')} {type(10)}")
print(f'{type('10')} {type(10)}')
print(type("10"),type(10))

#boolean data type
is_human=True
plays_cricket=False
print(f"{is_human} {plays_cricket}")
print(f"{type(is_human)} {type(plays_cricket)}")
print(type(is_human),type(plays_cricket))