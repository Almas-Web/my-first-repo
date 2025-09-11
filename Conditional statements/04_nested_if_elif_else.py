#Grade calculating 
student_score=int(input("Enter your mark : "))
if(student_score>80):
    print("Your grade is A+")
elif(student_score>70):
    print("Your grade is A")
elif(student_score>60):
    print("Your grade is A-")
elif(student_score>50):
    print("Your grade is B")
elif(student_score>40):
    print("Your grade is C")
elif(student_score>33):
    print("Your grade is D")
else:
    print("You are fail")
print("Exam ended!!!!!!!!!!!!!!!")


#calculator with nested condition
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operator=input("Enter an operator (+,-,*,/):")
if(operator=="+"):
    print(f"Result:{num1}+{num2}={num1+num2}") 
elif(operator=="-"):
    if(num1>num2):
        print(f"Result:{num1}-{num2}={num1-num2}")
    else:
        print(f"Result:{num2}-{num1}={num2-num1}")
elif(operator=="*"):
    print(f"Result:{num1}*{num2}={num1*num2}")
elif(operator=="/"):
    if(num2!=0):
        print(f"Result:{num1}/{num2}={num1/num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")
print("Program ended!!!!!!!!!!!!!!!")

#vowel or consonant check

character=input("Enter a character:")
if(character=="a" or character=="A"):
    print(f"The character {character} is a vowel")
elif(character=="e" or character=="E"):
    print(f"The character {character} is a vowel")
elif(character=="i" or character=="I"):
    print(f"The character {character} is a vowel")
elif(character=="o" or character=="O"):
    print(f"The character {character} is a vowel")
elif(character=="u" or character=="U"):
    print(f"The character {character} is a vowel")
else:
    print(f"The character {character} is a consonant")
print("Program ended!!!!!!!!!!!!!!!")

# Pythons's first philosophy is DRY (Don't Repeat Yourself)
# we can do the above program in a better way

character=input("Enter a character:")
if((character=="a"or character=="A") or 
   (character=="e" or character=="E") or 
   (character=="i" or character=="I") or 
   (character=="o" or character=="O") or 
   (character=="u" or character=="U")):
    print(f"The character {character} is a vowel")
else:
    print(f"The character {character} is a consonant")
print("Program ended!!!!!!!!!!!!!!!")


#using membership operator

vowels=[
'a','e','i','o','u','A','E','I','O','U'
]
character=input("Enter a character:")
if(character in vowels):
    print(f"The character {character} is a vowel")
else:
    print(f"The character {character} is a consonant") 
print("Program ended!!!!!!!!!!!!!!!")

#day in the week 
"""take a number from user and print the day name
1=Sunday"""
day_number=int(input("Enter a number (1-7):"))
if(day_number==1):
    print("Sunday")
elif(day_number==2):
    print("Monday")
elif(day_number==3):
    print("Tuesday")
elif(day_number==4):
    print("Wednesday")
elif(day_number==5):
    print("Thursday")
elif(day_number==6):
    print("Friday")
elif(day_number==7):
    print("Saturday")
else:
    print("Invalid day number! Please enter a number between 1 and 7.")
print("Program ended!!!!!!!!!!!!!!!")


#temperature 
temperature=float(input("Enter temperature in degree celsius:"))
if(-40<=temperature<0):
    print("Extremely Cold")
elif(0<=temperature<10):
    print("Very Cold")
elif(10<=temperature<20):
    print("Cold")
elif(20<=temperature<30):
    print("Normal")
elif(30<=temperature<40):
    print("Hot")
elif(40<=temperature<50):
    print("Very Hot")
elif(temperature>=50):
    print("Extremely Hot")
else:
    print("Invalid temperature")
print("Thankyou!!!!!!!!!!!!!!!")