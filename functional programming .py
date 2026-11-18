# It builds programs by combining the functions 
# the main purpuse of this is , makes programs easier to understand and predict them .

    #COMMON TOOLS :
""" MAP , FILTER , REDUCE 
MAP - It applies functionn to every item and produces the transformed items 
FILTER - it keeps only satisfied condition 
REDUCE - it combines items into single result

"""

# FIRSTCLASS FUNCTIONS 
""" The function which can be used like ordinary values is called firstclass functions ,like we can perforfm these things by fistclass fun
1- we can assign fun to a variable 
2- we can pass it as argument to another fun
3- we can return it from another fun

"""
numbers = [1,3,4,7,6,8,10]
doubled = list(map(lambda n:n*2,numbers))
evens = list(filter(lambda n:n%2 == 0,numbers))
total = ( lambda sum_so_far,n: sum_so_far +n,numbers,0)
print("doubled:",doubled)
print("evens:",evens)
print("total:",total)