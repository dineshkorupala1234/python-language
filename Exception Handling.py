# EXCEPTION HANDLING
# It will handles the unexpected errors at the time of executing a program 
# It helps in avoiding the crash directly , it will detects errors and manages it .
''' 1. TRY : In this block ,we can write any code which may throws a error
    2. EXPECT: If a error occurs in try block ,we use this to catch error and what to be done
    3. ELSE : If there is no error in try block , this esle will runs 
    4. Finally : This block will run for sure if there is error or not 
    
'''
    
try:
    number=int(input("Enter a number : "))
except ValueError:
    print("please enter the digits")
else:
     print("you entered :",number)
finally:
     print("it is done")       
    
    
