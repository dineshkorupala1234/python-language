#it indicates the data types of a parameters and return values , the type hints is a special syntax annotation 

def greet(name:str)->str:
    return f"hello,{name}!"
message :str = greet ("hey dinesh ! hello ")
print(message)

#FUNCTION ANNOTATION 
# It adds the type hints to parameters and return values 
def add(a:int,b:int)->int:
    return a+b
print(add(4,32))

# OPTIONAL
# Optional means a value can be either X type or NONE , its equal to X or None

from typing import Optional
def find_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "yogiii "
    return None
print(find_name(1))
print(find_name(2))

#UNION
#Union means it may be a variable or parameter value , so it may x type or y type

from typing import Union
def show_id(user_id:Union[int , str]) ->str:
    return f"ID:{user_id}"
print(show_id(43))
print(show_id("A43"))

#GENERICS
# It is place holder types which preserves a relation ship between input and output type
def first_item(items:list[str])->str:
    return items[0]
print(first_item(["blue","black"]))

#TYPING MODULE 
# It is a built-in module in a standard library , it provides the tools to label avdanced and complex data types 