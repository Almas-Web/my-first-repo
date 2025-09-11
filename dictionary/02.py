# Difficulty between bracket notation and get method

student={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

}
print(student.get("fater_name"))    # it will return None if key is not found
#print(student["fater_name"])         # it will return keyerror 
print(".............................")
# dictionary in list 
students =[
    {
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU"

    },
    {
    "name": "Ayan",
    "age": 22,
    "Roll" : 17,
    "University": "DU"

    },
    {
    "name": "Rahat",
    "age": 24,
    "Roll" : 37,
    "University": "RU"

    }

]

print(students[0].get("name"))
print(students[0].get("age"))
print(students[0].get("Roll"))
print(students[0].get("University"))

print(students[1].get("name"))
print(students[1].get("age"))
print(students[1].get("Roll"))
print(students[1].get("University"))

print(students[2].get("name"))
print(students[2].get("age"))
print(students[2].get("Roll"))
print(students[2].get("University"))
print(".............................")


# list in dictionary
student ={
    "name": "Almas",
    "age": 23,
    "Roll" : 27,
    "University": "BU",
    "courses": ["CSE101", "CSE102", "CSE103"]

}
print(student.get("name"))
print(student.get("age"))
print(student.get("Roll"))
print(student.get("University"))
print(student.get("courses"))
print(student.get("courses")[0])
print(student.get("courses")[1])
print(student.get("courses")[2])
print(".............................")


author ={
    "name": "Humayun Ahmed",
    "age": 66,
    "Books" : ["Nondito Noroke", "Shonkhonil Karagar", "Deyal", "Misir Ali"],
   "Children": [
        {
            "name": "Shomi",
            "age": 30
        },
        {
            "name": "Shila",
            "age": 28
        }
    ]
}
print(author.get("name"))
print(author.get("age"))
print(author.get("Books")[0])
print(author.get("Books")[1])
print(author.get("Books")[2])
print(author.get("Books")[3])
print(author.get("Children")[0].get("name"))
print(author.get("Children")[0].get("age"))
print(author.get("Children")[1].get("name"))
print(author.get("Children")[1].get("age"))
print(".............................")

student_data={
    "names": ["Almas", "Ayan", "Rahat"],
    "ages": [23, 22, 24],
    "Rolls" : [27, 17, 37],
    "Universities": ["BU", "DU", "RU"]
}
print(student_data.get("names")[0])
print(student_data.get("ages")[0])
print(student_data.get("Rolls")[0])
print(student_data.get("Universities")[0])
print("-----------------")
print(student_data.get("names")[1])
print(student_data.get("ages")[1])
print(student_data.get("Rolls")[1])
print(student_data.get("Universities")[1])
print("-----------------")
print(student_data.get("names")[2]) 
print(student_data.get("ages")[2])
print(student_data.get("Rolls")[2])
print(student_data.get("Universities")[2])
print(".............................")


company={
    "name": "Google",
    "founded": 1998,
    "employees": [
        {
            "name": "Alice",
            "position": "Software Engineer"
        },
        {
            "name": "Bob",
            "position": "Product Manager"
        }
    ]
}
print(company.get("name"))
print(company.get("founded"))
print(company.get("employees")[0].get("name"))
print(company.get("employees")[0].get("position"))
print(company.get("employees")[1].get("name"))
print(company.get("employees")[1].get("position"))
print(".............................")

# dictionary with list

author={

    "name" : "almas",
    "books" :["one", "two"],
    "children" :[
               {"name":"nuhas", "age":20},
               {"name" : "abir" , "age":30}
 ]
}

print(author.get("name"))
print(author.get("books"))
print(author.get("books")[0])
print(author.get("books")[1])
print(author.get("children")[0].get("name"))
print(author.get("children")[0].get("age"))
print(author.get("children")[1].get("name"))
print(author.get("children")[1].get("age"))
print(".............................")


# nested dictionary
companys = {
    "mobile_operator": {
        "grameenphone": {
            "services": ["internet", "sms", "voice call"]
        },
        "teleTalk": {
            "services": ["internet", "sms", "voice call"]
        }
    }
}

# Accessing mobile operators
mobile_operators = companys.get("mobile_operator")

# Grameenphone details
grameenphone_details = mobile_operators.get("grameenphone")
grameenphone_services = grameenphone_details.get("services")
print("Grameenphone Services:", grameenphone_services)
# Teletalk details
teletalk_details = mobile_operators.get("teleTalk")
teletalk_services = teletalk_details.get("services")
print("Teletalk Services:", teletalk_services)
print("Thank you")
print(".............................")
# Directly accessing nested values

print(companys.get("mobile_operator").get("grameenphone").get("services")[0])
print(companys.get("mobile_operator").get("grameenphone").get("services")[1])
print(companys.get("mobile_operator").get("grameenphone").get("services")[2])
print(companys.get("mobile_operator").get("teleTalk").get("services")[0])
print(companys.get("mobile_operator").get("teleTalk").get("services")[1])
print(companys.get("mobile_operator").get("teleTalk").get("services")[2])
print(".............................")