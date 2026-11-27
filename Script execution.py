# The term script execution means running a python file , so python carries instructions into it from top to bottom 
'''A python file can be used in two ways
1. run as script : python hello.py
2. imports as module : another python fle uses import hello
'''

# if__name__="main__"
# Before runing a file in python , interpreter sets a special variable , one of them is __name__


# RUNNING A FILE DIRECTLY
print("always executes ")
if __name__:"main__"
print("executed when invoked directly")
print("executed when imported ")    

# importance of using if__name__="main__"
def my_function():
    print("i am inside function")
my_function()    

#COMMAND LINE ARGUMENTS
# This are lines passed to a script when running it in terminal or in t rhe command prompt
# they acts like inputs that allows to change progams behaviour without modifing code 

#ARGPARSE MODULE 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="dinesh kumar ")
args = parser.parse_args()

print(f"Hello, {args.name}!")


