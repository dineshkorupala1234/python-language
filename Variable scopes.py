#The location where we can find variable and also we can access it if we need is called the scope of variable 

#LOCAL VARIABLE 
# If a variable created inside a function that belong to function local scope 
# they exist only while function runs and cant accesss from outside 

def localscope():
    name = "dinesh kumar " # here the variables declared inside 
    age = 22
    print(name,age)
localscope()

#GLOBAL SCOPE 
# A variable can be declared inside and outside of function 

def globalscope():
    name = "chintu"   # here we can give variable inside or outside 
    age = 20
    print(name,age)
globalscope()

#if we want to define 2 variables , one is inside and one is outside , we just use the global keyboard

#NON LOCAL SCOPE 
# this keyword used to modify a variable belonging to its nearest elclosing function
# oka function lopala inko function unapudu inner function nunchi outer function variable modify cheyadaniki non local use chestam 

#LEGB RULE
""" local , Enclose , Global , Built in
this rule is used to check variable
1 . LOCAL - it is used to search variable in current function
2 . ENCLOSING -it searches in outer or enclosing function 
3 . GLOBAL - It searches in the outer function 
4 . Built in - it will search in sum(),len(), print
"""