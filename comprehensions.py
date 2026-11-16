#It is a short way to create a new collection like (list , dict , set),out of an existing one in a single line of code 
# it is used in data processing , web development and automation tasks 
# reduces errors by minimizing line of code 

                  #NEED TO REVISE 
                   
#LIST COMPREHENSION 
# it creates a new list from items in another collections 

 # genrating list of even numbers 
a= [1,2,3,4,5,6,7,8,9]
res = [num for num in a if num%2 == 0]
print(res) #it creates list of even numbers by checking elements in a ,which are divisible by 2 

#DICTIONARY COMPREHENSION 
# it makes dictionary of key value pairs 
 
#genrating dict of numbers and cubes 
res = { num : num **3 for num in range(1,8)}
print(res)  # it creates dict where keys are numbers from 1 to 5 , and values are there cubes

#SET COMPREHENSIONS 
# it makes a set of unique result 
# it automatically eliminates duplicates

#extracting even numbers
a = [1,2,2,3,4,4,5,6,6,7,8]
res = {num for num in a if num%2 == 0}
print(res) 

# GENRATOR COMPREHENSION
# it provides result one at a time as we use them 
doubles = (n*2 for n in [1,2,3,4])
print(list(doubles))