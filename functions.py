# it is a reusable block of code used to perform specific task 
# they help in organising programs into smaller section and execute same logic when needed 
# it can be defined using def keyword
    
def greet(dinesh):
    message = "what is going on, " + dinesh
    return message
greeting = greet("dinesh")
print(greeting)

#Uses of functions
# code reusability
# modularity
# readability
# maintainability

# CALLING A FUNCTION 
# after creating function ,call it by using the function followed by parenthesis()
# Function call
message = greet("dinesh")
print(message)

#RETURN
#It is a keyword used to sendn a result from a function back to the place where function was called 