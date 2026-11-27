#Genrators are the function that returns valus at once using YIELD Keyword , instead of storing all values in memory 
# They provide efficient way to handle large data sets and sequences 

def count_numbers():
    for num in range (1,6):
        yield num
for value in count_numbers():
 print(value)
            
#YIELD
# To Make generator function we use yield , each time python reaches yeild it and returns that value and pauses the function and the next request resumes it where it stopped

def count_up (limit):
    number =1
    while number <= limit:
        yield number
        number +=1
numbers=count_up(5)  #this fun has not run through its loop yet 
print(next(numbers))
print(next(numbers))
print(next(numbers))                    

#YIELD FROM
# This expression used inside a generator function to assign part of its execution to another generator or iterable
def letters():
    yield from("a","b","c","d")
print(list(letters()))    

#GENERATOR FUNCTIONS
#This is a python function that uses yield to produce values , one at a time 

def even_numbers(limit):
    for number in range(0,limit + 1,2):
        yield number
even = even_numbers(6) 
print(next(even))
print(next(even))
print(next(even))
print(next(even))

# LAZY EVALUATION 
# just by calling generator function doesn't calcuate all its values at once , it creates a genrator object and each next() makes it calcuate just the next value

def numbers():
    print("making 1")
    yield 1
    print("making 2")
    yield 2
g= numbers ()
print(next(g))
print(next(g))    
       