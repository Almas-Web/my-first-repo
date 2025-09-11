# syntax 
"""
if condition:
    if block
else:
    else block
"""

print("Election started")
user_age=int(input("Please enter your age: "))
if (user_age>=18):
    print("You can vote!!!!")
else:
    print("You can't vote....")
print("Election  ended.")

#even and odd number 
number=int(input("Please enter a number:"))
if(number % 2==0):
    print("Even number.")
else:
    print("Odd number.")
    
# another way 
number=int(input("Please enter a number:"))
if(number %2 !=0):
    print("odd number")
else:
    print("Even number ") 

# another way 
number=int(input("Please enter a number:"))
if(number % 2 == 1):
    print("Odd number")
else:
    print("evene number")
