# List of a list 
persons=[ 
    ["Almas","Tuba","Tanim"],                                 # 0 index
    [23,22,21],                                               # 1 index
    ["Bangladesh","India","Pakistan"],                        # 2 index
    ["almas@gmail.com","tuba@gmail.com","tanim@gmail.com"]    # 3 index
]
print(persons)
print(persons[0][1])


person=[
    ["Almas",23,"Bangladesh","almas@gmail.com"],
    ["Tuba",22,"India","tuba@gmail.com"],
    ["Tanim",21,"Pakistan","tanim@gmail.com"]
]
print(person)
print(person[0][0])
print(person[0][1])
print(person[0][2])
print(person[0][3])
person[0][0]="Almas Hossain"
print(person[0])
print(f"My name is {person[0][0]}.My age is {person[0][1]} years old.I live in {person[0][2]}.My email is {person[0][3]}")

person.append(["Sakib",24,"Sri Lanka","sakib@gmail.com"])
print(person)
person.extend([["Anika", 25, "Nepal", "anika@gmail.com"]])  # Adds as one list
print(person)
person.insert(1, ["Hasan", 26, "Bhutan", "hasan@gmail.com"])
print(person)
person.remove(["Tuba", 22, "India", "tuba@gmail.com"])
print(person)
person.pop()  # removes last list
print(person)