"""
*****
*****
*****
*****
"""
number_of_rows = 4
number_of_star = 5
for i in range(1,number_of_rows+1):
    for j in range(1,number_of_star+1):
        print("*") # by default print function will add new line after every print
    
number_of_rows = 4
number_of_star = 5
for i in range(1,number_of_rows+1):
    for j in range(1,number_of_star+1):
        print("*",end="" ) # by default print function will add new line after every print

number_of_rows = 4
number_of_star = 5
for i in range(1,number_of_rows+1):
    for j in range(1,number_of_star+1):
        print("*",end="" ) # by default print function will add new line after every print
    print() # this will add new line after every row

"""
*
**
***
****
*****
"""
row=5
for i in range(1,row+1):
    for j in range(i):
        print("*",end="") # by default print function will add new line after every print
    print() # this will add new line after every row

row=10
for i in range(1,row+1):
    for j in range(row-i+1):
        print("*",end="") # by default print function will add new line after every print
    print() # this will add new line after every row