# Closures and Decoarators in python are powerful features in python that allow advanced and flexible code patterns 

# CLOSURES 
# A closure is a function that remembers value from scope where it was created , even after the outerfunction stopped running  
def outer():
    message = "Namastey hyderbad"
    def inner():
        print(message)
    return inner
result = outer()
result()

#  - DECORATOR -  it uses the closure to remember the function it wraps
    
# FUNCTOOLS.WRAPS
# It keeps orginal function name and documetation on the wrapper

from functools import wraps

def announce(func): #DECORATOR
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished!")
        return result
    return wrapper

@announce
def note(name):
    """Hey, What's up .""" 
    print(f"hey man you are , {name}!")

note("Dinesh")
print(note.__name__) 
print(note.__doc__)   