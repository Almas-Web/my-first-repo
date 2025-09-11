# Case sensitive 
name1 ="Almas"
name2 ="almas"
name3="Sakib"
name4="sakib"
name5="almas"
print(name1==name2)
print(name3==name4)
print(name2==name5)
print("-----------------------------------")

import time 
is_logged_in=True
print("Hi you are logged in")
print("You can browse ")
time.sleep(2)
print("You have been logged out")
is_logged_in=False
print("You are logged in:", is_logged_in)
print("-----------------------------------")

# type casting 
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