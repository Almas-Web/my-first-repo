my_country = "Bangladesh"
my_name="Almas"
my_age=23 
my_email="almas@gmail.com"
print(my_country)
print(my_name)
print(my_age)

print("I live in" +my_country)
print("I live in" +" "+ my_country)
print(my_country +" " "is a beautiful country")
print("My country"+' '+ my_country+' '+ "is a beautiful country")
print(my_country +" "+ "is an Independent country ")

# string formating 
print(f"I live in {my_country}")
print(f"{my_country} is a beautiful country ")
print(f"{my_country} is too big ")
print(f"My name is {my_name}.My age is {my_age}.My email is {my_email}")
print(f"My name is {my_name}.My age is {my_age}.My email is "+ my_email)

#Multiple output 
print(f"""
 My name is {my_name}.
 My age is {my_age}.
 My country name is {my_country}.
My email is {my_email}
""")

print(f"""
 My name is {my_name}.
                                     My age is {my_age}.
              My country name is {my_country}.
                                               My email is {my_email}
""")