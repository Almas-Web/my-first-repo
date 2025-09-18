# multiplication_table of 5
number = 5
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
print("....................")

n1=2
n2=4
for number in range(n1,n2+1):
    print(f"Multiplication table of {number}")
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")
print("....................")

n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
for number in range(n1,n2+1):
    print(f"Multiplication table of {number}")
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")