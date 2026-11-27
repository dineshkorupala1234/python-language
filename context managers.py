# context managers means an object , that automatically setsup and tearsdwon resources , it is done around a block of code 
''' How to create a context manager
1. using @contextmanager and yield
1. using a class (__enter__ and __exit__)
'''
# WITH STATEMENT

#with open("sets.py","w")as file:
 #   file.write("hello")

#CONTEXTLIB
# It is a stanadrd library module , it makes it easier to create and work with context managers

from contextlib import contextmanager
@contextmanager
def temparary_message():
    print("starting")
    try:
        yield
    finally: 
      print("cleaning up")
with temparary_message():
    print("inside the block")        
    
# CUSTOM CONTEXT MANAGER 
# This is a user defined class or function , that implements pythons context management protocol

#defining class with __enter__ and __exit__

def __enter__(self):
    print("setting it ")
    return self
def __exit__(self,exc_type,exc_value,traceback):
    print("cleaning up")
    return False
print("using resource")
           
    
        
    
