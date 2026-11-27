# PYTYHON STANDARD LIBRARY 
''' It is a collection of modules included with python , we can use them without installing extra packages 
'''
# SYNTAX : import module_name
import math
print(math.sqrt(5)) 

# MATH MODULE 
# This module pre defined mathematical function and constants to perform maths calcuations 

#RANDOM MODULE
#It is used to genrate random numbers and also it selects random elements from the sequences 

import random
print(random.random())
print(random.randint(1,11))
print(random.randrange) 
print(random.shuffle)

#DATE TIME MODULE
# it is used to work with dates and times 

#CURRENT DATE AND TIME 
import datetime
now = datetime.datetime.now()
print(now)

#CREATING OUR OWN DATE 
import datetime
mydate=datetime.date(2004,5,16)
print(mydate)

#TIME MODULE 
#It provides function to work with time related operations , like getting current timestamp, delays and measuring execution time
import time
print("hello ")
time.sleep(4)
print("welcome")

#COLLECTIONS MODULE 
# This provides usefull data structures that complement built-in types such as list,dict,tuple etc
from collections import Counter
numbers=[1,2,3,2,3,4,3]
result=Counter(numbers)
print (Counter)

from collections import deque
number = deque([10,29,49])
numbers.append(40)
numbers.append(5)
print(numbers)

#ITERTOOLS
# This module provides functions to create efficient iterators for looping , combination , permutations and repeated operations 
import itertools
for i in itertools.count(1):
    print(5)
    if i == 5:
      break
  
 #FUNCTOOLS MODULE
 # This module provides higher order functions and tools for working with functions and collable objects  