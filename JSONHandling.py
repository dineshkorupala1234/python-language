# JSON - JAVA SCRIPT OBJECT NOTATION 
# JSON handling means reding , writting and creating json data in a pyhton programming 
# it is a text format , commonly used to store data and exchange it between programs 
# NOTE : to perform any opeartion first we should create a json file and we should give values there . then after we can call them using the json file name 


# FUNCTIONS 
# JSON LOAD(FILE)
# it reads json from a open file and converts it to a python object


import json

with open("data.json","r") as file:
    student = json.load(file)
print(student)
print(student["name"])

#LOADS FUNCTION 
# we shoulds use here json.loads(json_text)


import json

json_text = '{"name": "Dinesh", "age": 22}'
student = json.loads(json_text)

print(student)
print(student["name"])


