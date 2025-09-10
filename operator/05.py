# type casting 
# string to integer
num1="10"             # "a"  dont works string to integer
print(type(num1))
number1=int(num1)
print(number1)
print(type(number1))

# integer to string
num2=20
print(type(num2))
number2=str(num2)
print(number2)
print(type(number2))

#float to integer
num3=10.5
print(type(num3))
number3=int(num3)
print(number3)
print(type(number3))

# we can only concetenate string with string not with integer

user_name="Almas" 
user_age=23
#print("My name is "+user_name+" and my age is "+user_age)  # error
print("My name is " + user_name+ "." + "I am only " +str(user_age) + "years old ")
print("-----------------------------------")
# we can directly print this by f string
print(f"My name is {user_name}. I am only {user_age} years old")
print("-----------------------------------")

user_age =input("Enter your age :" )
user_age=int(user_age)
condition=user_age>=18
print("You are eligible:", condition)
print("-----------------------------------")

# direct use 
user_age =int(input("Enter your age : "))
condition=user_age>=18
print("You are eligible:", condition)
print("-----------------------------------")
