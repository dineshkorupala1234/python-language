#INSTANCE METHOD :
''' we use self here , it can use or change data belong to that particular object
self: self is a specific object that is currently using the method 
ex : cat.describe()
- it passes Cat as self automatically
'''
#CLASS METHOD
''' It is defined with @classmethod
it can use or change class level data 
ex: cat.get_sepcies()
'''
#STATIC METHOD 
'''They are defined with @static method 
It acts like helper function stored inside a cls to organise it ,it will not accesss or modify any object
'''
class cat:
    species ="pet"
    def __init__(self,name):
        self.name=name
    def describe (self):
        return f"{self.name} is a {self.species}"  
    @classmethod
    def get_species(cls):
        return cls.species
    @staticmethod
    def valid_name(name):
        return bool(name.strip()) 
my_cat = cat("johny")
print(my_cat.describe())                   
print(cat.get_species())                
print(cat.valid_name("Rocky"))    