''' FILE HANDLING 
it means performing a opeartion on a file such as creating , opening , reading and writting 
'''
# syntax for opening and closig 
# opening : file = open(filename.txt,"mode")
            # f = open("dinesh.txt","r")
# closing : file = open(filename.txt,"mode")
            # f = open("dinesh.txt","r")
            # file.close()
            
 #READING A FILE IN READ MODE "R"
file = open("lists.py","r")    # here we can read lists file data by reading mode
content = file.read()
print(content)
file.close()    

# WRITING TO A FILE 
#we cn add content to file 
# writing a file is done using mode 'w'
with open("lists.py","w") as file:
    file.write("hello,good morning\n")
    file.write("lists are easy")
print("file written sucessfully")    

#APPENDING TO A FILE 
# adding new data to end of file without erasing or overwritting it 
# we use "a", to add content to file  

with open ("lists.py","a",encoding="utf-8")as file :
    file.write("another note\n")       
print("it is done ")       

#THE WITH STATEMENT
''' with - opens a file for a block of code and closes automatcally when block ends
    even if error occurs , it helps to prevent and proceeds 
'''

#ENCODING
''' it is the processing of converting human readble text(str) into binary types
'''
with open("lists.py","wb") as file:
    data= file.read()