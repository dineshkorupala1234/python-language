# Recrusion is the process in which a function calls it self repeatdly untill condition satisfy's
""" 1- It breaks large programs in to smaller 
2- like if we want to print numbers from 1 to 5 we genrally use loops , but here recrusin it self calls the function untill it prints numbers 
"""

# BASE FUNCTION 
# - it is the condition that stops recrusion from caling it self after the fun gets satisfied 
# BASE CONDITION is nothing but stopping the fun

def countdown(n):
    if n == 0: # base condition applied here .
        print("it is done")
    else:
        print(n)
        countdown(n-1) #recrusion 
countdown(3)

