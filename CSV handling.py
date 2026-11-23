# CSV - COMMA SEPERATED VALUE 
# It is the process of reading , writting, modifing a comma seperated values (.csv) files 
# it stoes the information in rows and columns with the values seperataed by a comma's

#READING CSV FILE 
import csv
with open("students.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name","age","city"])
    writer.writerow(["dinesh", "22", "nagarkurnool"])
    writer.writerow(["yogi", 20, "gadwal"])
with open("students.csv","r",newline="",encoding="utf-8")as file :
    reader=csv.reader(file) 
    for row in reader:
        name = row[0]
        age = row[1]  
        city = row[2]
    print("Name:", name, "Age:", age,"City:", city)

#WRITING A CSV FILE 
# it means we are assigning the values which are going to return as table format after reading is done 

import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name","age","city"])
    writer.writerow(["dinesh", "22", "nagarkurnool"])
    writer.writerow(["yogi", 20, "gadwal"])
print("name:","age:","city")   

#USES OF CSV FILE
'''1 . to store small tables like student records 
   2 . to transfer data between programs 
   3 . to save simple reports and results 
   4 . to work with data that has rows and columns 
'''
