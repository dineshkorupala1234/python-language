#COMPOSITION 
# Other classes oka object ni use cheskoni inko kotha class ni build cheyadame python lo composition antaru 
# To know relation ship between classes we use 'has-a' in composition 
# Objects ni inter change cheyadaniki edi flexible ga work chestadi 
class engine:
    def start(self):
        print("engine started")
class car:
    def __init__(self):
     self.engine=engine()
car = car()
car.engine.start()
                 
#PROPERTIES
# Property anedi oka special class attribute,edi oka method normal variable laga use cheyadaniki and background lo custom logic ni run cheyadaniki use avthadi 
# deeni @property decorator tho create chestam
 
class person:
    def __init__(self,age):
        self.age = age
@property
def age(self):
    return self.age
@age.setter
def age(self,value):
    if value<0:
     raise value 
    self.age = value
    person = person(20)
print(person,age)

#GETTERS
# It is used to read the value of a variable
# edi oka sepcial method , oka class lopala unna private data ni safe ga chadavadanki getters use chestam

class years:
    def __init__(self,age=0):
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
raju = years()
raju.set_age(25)
print(raju.get_age())
print(raju._age)
        
#SETTERS
# It is used to set or update the value 
# Oka variable ki kotha value ni assign cheyadaniki leda update cheyadaniki setters use chestam         