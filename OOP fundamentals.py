# Object Orriented programming empowers developers to build applications 
# OOP'S is a way of organising code that uses classes and objects to represent real world entities
 
# CLASS
''' Class is a blue print used to create a object 
ex: taking desgin from engineer before building a house , same here class works like that  
''' 
#OBJECT
''' objcect is just a instance of a class , genrally object created using a blueprint
- EX: If student is class ,student ane class nunchi object create chestam 
'''
#ATTRIBUTES
# Attributes are stored data in an object like name ,age etc
""" TYPES OF ATTRIBUTES
1.Instance attribute : it Belongs to one specific object , different objects can have diff values
2.class attribute : it belongs to the class shared by its objects untill object overrides it .

 """
class student:
    name="dinesh"
    years=22
    s1=()
    print(name)
    print(years)
    
   #with attribute
    
class Cat:
    pets= "Cat"    
    def __init__(self,name):
     self.name = name
cat1 = Cat("rocky")
cat2 = Cat("candy")

print(cat1.name)
print(cat2.name)

    