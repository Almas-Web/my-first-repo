# Assingment print --My name is ALmas. I am 23 years of old .I get 1000tk per month.
# My email is almashossen67@gmail.com   --- using list

myself=[
    ["Almas"],
    [23],
    ["almas67@gmail.com"],
    [10000],
]

# method-1
print(f"My name is {myself[0][0]}. I am {myself[1][0]} years of old. I get {myself[3][0]}tk per month. My email is {myself[2][0]}.")

user_name= myself[0][0]
age=myself[1][0]
email=myself[2][0]
salary=myself[3][0]

# method-2
print(f"My name is {user_name}. I am {age} years of old. I get {salary}tk per month. My email is {email}.")
