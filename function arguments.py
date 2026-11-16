#The arguments are values passed to a function when it is called , they follow functions to recive input data and perform opeartions 
# SYNTAX
#def function name(arguments)
 #    fun body 
  #   return value

def evenodd(x):
    if(x %2 == 0):
        return "even number"
    else:
        return "odd number"
print(evenodd(16))
print(evenodd(7))
    
 #TYPES OF ARGUMENTS 
 # 1.DEFAULT ARGUMENTS
 # When no value is called during function call, it uses predefined value
  
def myfun (x,y = 50):
    print("x:",x)
    print("y:",y)
myfun(10)  

#KEYWORD ARGUMENTS
# It passes values using parameter names, so argument does not matter
def student(aname,bname):
 print(aname,bname)
student(aname = 'hello',bname = 'dinesh')
student(aname ='good',bname ='morning')

#POSITIONAL AGRUMENTS
#Here the values are assigned to parameters based on their functional call

def nameheight (name, height):
     print("Hlo ,my self",name)
     print("my height is ",height)
     
print("case-1:")
nameheight("dinesh",5.5)

print("case-2:")
nameheight (22,"dinesh")

#ARBITARY ARGUMENTS
#it allows function to acceptmultiple values 
# this is done using the special symbols
 # 1- *args-collects the extra positional arguements as tuples
 # 2 - **kwargss - it collects the extra keyword arguments as dictionary 
  
def allscores(*args,**kwargs):
 print("scores:",args)
 print("student details:",kwargs)
allscores(211,134,name="dinesh",subject="science")

# here 211 and 134 collected by *args as tuple
# name and subject are collected by **Kwargs as dictionary 
