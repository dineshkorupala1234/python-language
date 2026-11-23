# A Dunder method means "double underscope method " like there names start with double underscores and ends with double underscore 
# ex: __init__   , __str__

''' common dunder methods
1.__init__  = when we create object ,it will run automatically and initilizes the variables
2.__str__   = if we want to print any object , it will return in string 
3.__len__   = this fun tells the length of object 
4.__add_    = it defines how objects of class is added by using + OPERATOR 
5.__repr__  = it will returns the official string representation
6.__eq__    = it is used to check wheather two ojects are equal or not by using  == OPERATOR 

'''

class book:
    def __init__(self,title):
        self.title_title
    def __str__(self):
        return self.title
    def __len__(self):
        return len(self.title)
    book = ("Story of akbar and birbal") 
    print(book)
    print(len(book))
    print(str(book))
      
