# MODULE 
# module is simply a python file , like we can store variables , funcctions , classes and we can reuse in another programs 
# TYPES OF MODULES : BUILT-IN MODULES - the default modules are known as built-in modules 
                     # USER DEFINED MODULES : the modules created by us is known as user defined modules 
                     # THIRD PARTY MODULES : The modules which are installed by pip 
                     
# PACKAGES 
# Package is simply a folder in packages there will be 1 or more .py files or modules 
# Use of packages : better structure , no naming conventions 
                     
                     
#Here we created a custom module for our program , instead of using the in built modules                  
import maths_operations
print(maths_operations.add(20,30))
print(maths_operations.sub(20,30))
print(maths_operations.mul(20,30))
                     
# Ways of importing modules
# the maths is a built in module 
import math
print(math.sqrt(25)) 

# METHOD 2 : instead of importing full module , we import which we want 
from math import sqrt,pi
print(sqrt(25))
print(pi)

# CUSTOM MODULES
# Custom module (user defined module)
'''def say_hello(name):
    return f"hello,{name}!"
'''
def add(a,b):
    return a+b
import greetings
import maths_operations as tools
from greetings import say_hello
from maths_operations import add
print(greetings.say_hello("dinesh"))
print(tools.add(3,1))
print(tools.mul(20,83))
print(tools.sub(23,12))
print(say_hello("dinesh"))
print(add(10,28))
 
