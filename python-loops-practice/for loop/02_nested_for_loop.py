# nested for loop 
for i in range(2): # outer loop
    for j in range(3): # inner loop
        print(f"i={i}, j={j}")

# for loop with break and continue
for i in range(10):
    if i==5:
        break # exit the loop when i is 5
    if i%2==0:
        continue # skip even numbers
    print(i) # print only odd numbers less than 5

#for loop with else and break
nums=[1, 2, 3, 4, 5]
for  n in nums:
    if n==5:
        print("Found 5")
        break   
else:
    print("6 not found in the list")



# for loop+condition+enemerate+zip
names=["Tanim","Rafi", "Sakib", "Rana"]
marks=[85, 30, 78, 39]
passing_marks=40
for index, (name, mark) in enumerate(zip(names, marks), start=1):
    if mark>=passing_marks:
        result="passed"
    else:
        result="failed"
    print(f"{index}. {name} scored {mark} and {result}")

# vowel and consonant count in a string

country="bangladesh"

count_vowel=0
count_consonent=0

vowels=["a","e","i","o","u"]

for character in country:
    if(character in vowels):
        count_vowel=count_vowel+1
    else:
        count_consonent=count_consonent+1
print(f"Total vowel={count_vowel}\nTotal consonent={count_consonent}")