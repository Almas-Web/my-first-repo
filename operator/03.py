# comparison operators

x=10
y=7
print("Equal:", x==y) 
print("Not equal:", x!=y)
print("Greater than:", x>y)
print("Less than:", x<y)
print("Greater than or equal to:", x>=y)
print("Less than or equal to:", x<=y)
print("-----------------------------------")

# is operator 
user_name="Almas"
checked=user_name is None 
print(checked)
print("-----------------------------------")
user_name=None
checked=user_name is None 
print(checked) 
print
is_logged_in =True
checked1=is_logged_in is True
checked2=is_logged_in is False 
print(checked1)
print(checked2)
print("-----------------------------------")
is_logged_in =False
checked1=is_logged_in is True
checked2=is_logged_in is False
print(checked1)
print(checked2)
print("-----------------------------------")

num=10 
ls=["Almas","Sakib","Rony"]
example=None
print(num is None)
print(ls is None)
print(example is None)
print("-----------------------------------")

# or, and , not operators

user_age=18
user_gender="male"
condition1=user_age>=18
condition2=user_gender=="male"
print(condition1 or condition2)
print(condition1 and condition2)
print(not condition1)
print(not condition2)
print("-----------------------------------")

is_subscribed=True
is_logged_in=True
print(is_subscribed and is_logged_in)
print(is_subscribed or is_logged_in)
print(not is_subscribed)
print(not is_logged_in)
print("-----------------------------------")