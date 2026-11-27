# ITERATORS : It is a collections such as list , tuples 
# two important methods : __iter__() > it returns iterator object by it self
#                        __next__()  >it returns next itme in list , and returns STOPITERATION errpr when items over


# ITER() : This is used to change one iterable to iterator 
#NEXT()  : It returns items one by one in a iterator 

# CODE OF __next__()

fruits = ["grapes","apple"]
fruit_iter = iter(fruits)
print(next(fruit_iter))  
print(next(fruit_iter)) 

#STOPITERATION 
# This is in-built iteration , in a iterator if all itesm are over this tells us that no items are there in iterator
# and this raises a stopiteration error

# TRY -EXPECT
# When we using next(),this try expect helps to avoid the crash 