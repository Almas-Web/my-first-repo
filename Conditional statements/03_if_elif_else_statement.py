#Syntax 
"""
if condition:
    if block
elif condition:
    elif block
else:
    else block 
"""

# zero positive and negative number 
number=int(input("Enter a number :"))
if(number== 0):
    print("Zero number")
elif(number>0):
    print("positive number")
else:
    print("Negative number")
print("Program ended!!!!!!!!!!!!!!!")

# find greatest ,smallest,equal number 
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
if(num1>num2):
    print(f"The greatest number is:{num1}")
elif(num2>num1):
    print(f"The greatest number is : {num2}")
else:
    print("Both numbers is equal ")
print("Program ended!!!!!!!!!!!!!!!")



#find the largest number among three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if(num1>num2) and (num1>num3):
    print(f"The largest number is :{num1}")
elif(num2>num1) and (num2>num3):
    print(f"The largest number is :{num2}")
elif(num3>num1) and (num3>num2):
    print(f"The largest number is :{num3}")
else:
    print("All numbers are equal") 
print("Program ended!!!!!!!!!!!!!!!")

#find the smallest number among three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if(num1<num2) and (num1<num3):
    print(f"The smallest number is :{num1}")
elif(num2<num1) and (num2<num3):
    print(f"The smallest number is :{num2}")
elif(num3<num1) and (num3<num2):
    print(f"The smallest number is :{num3}")
else:
    print("All numbers are equal")
print("Program ended!!!!!!!!!!!!!!!")

# find the number is divisible by 5 and 11 or not
number=int(input("Enter a number:"))
if(number % 5==0) and (number % 11==0):
    print(f"The number {number} is divisible by 5 and 11")
else:
    print(f"The number {number} is not divisible by 5 and 11")
print("Program ended!!!!!!!!!!!!!!!")


#leap year check 
year=int(input("Enter a year:"))
if(year % 4==0) and (year % 100 !=0) or (year % 400==0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
print("Program ended!!!!!!!!!!!!!!!")


# simple login system
user_name="admin"
user_password="12345"
input_name=input("Enter your name:")
input_password=input("Enter your password:")
if(input_name==user_name) and (input_password==user_password):
    print("Login successful")
else:
    print("Invalid username or password")
print("Program ended!!!!!!!!!!!!!!!")


#another way 
user_name="admin"
user_password=12345
input_name=input("Enter your name:")
input_password=int(input("Enter your password:")) #convert string to integer
if(input_name==user_name) and (input_password==user_password):
    print("Login successful")
else:
    print("Invalid username or password")
print("Program ended!!!!!!!!!!!!!!!")














