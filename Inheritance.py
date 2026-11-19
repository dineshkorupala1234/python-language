#The existing class is called parent class 
# The new class is called child class
''' SINGLE INHERITANCE 
1. When a child class is derived from one parent class 
2. The child class recives the function from parent class 
'''
class parent:
    def func1 (self):
        print("This fun is in parent class")
class child(parent):
    def func2(self):
        print("This fun is from child class")
obj = child()
obj.func1()
obj.func2()                

#MULTIPLE INHERITANCE 
''' When a child class inherits from two or more parent classes that is called multiple inheritance
ex: child class derived from parent class1 , parent cls 2 
'''
class mother:
    mothername = " "
    def mother(self):
        print(self.mothername)
class father: 
    fathername = " "
    def father(self):
        print(self.fathername)
class son(mother,father):
    def parents(self):
        print("father:",self.fathername)
        print("mother:",self.mothername)
s1 = son()
s1.fathername="Ramakrishna"
s1.mothername="Sumithra"
s1.parents()    
#son inherits from mother and father
# it can access both mother name and father name 
 
#METHOD OVERRIDING
# Manam oka parent class lo unna method ni ,same daani oka child class lo use chestey appudu overriding anedi jarguthadi 

class animal:      #parent class
 def speak(self):    #parent method
    print("same sound")
class cat(animal):    # child class
 def speak(self):       # child method
    print("Meow Meow ")   
cat = cat()
cat.speak() 
    
#SUPER
# Manam parent class nunchi em ana method call cheyadaniki e function ni use chestam

class parent :
    def show(self):
        print("this is a parent class method ")
class child:
    def show(self):
     super().show()    # called child method from parent class
    print("this is a child class method")
    obj=child()
    
             
         
        
        
       
