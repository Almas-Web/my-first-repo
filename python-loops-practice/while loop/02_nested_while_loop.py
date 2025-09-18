#nested while 
i=1
while (i<=3):
    j=1
    while (j<=2):
        print(f"i={i}, j={j}")
        j+=1
    i+=1

# Nested while loop example
# Printing a multiplication table (1 to 5)

i = 1
while i <= 5:   # outer loop
    j = 1
    while j <= 5:   # inner loop
        print(f"{i} x {j} = {i * j}")
        j += 1
    print("-----")  # separate each row
    i += 1

