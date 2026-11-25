# Genrally , Regular Expressions are the patterns used to find , check , or to replacev text 
# in python , the built-in re module provides regular expression tools 

import re #regular exprsesion
text = "cat 93,dog 79"
print(re.search(r"\d+",text).group())
print(re.match(r"cat",text).group())
print(re.findall(r"\d+",text))
print(re.sub(r"\d+","are pets ",text))

''' 1. re.module - import re - used to search match file and replace text 
    2. re.search - it finds first match anywhere in the text 
    3. re.match - it checks for the match only at the begining of the text 
    4. re.findall - it runs a list of matches 
    5. re.sub - it replaces the matches with the replacement text 
'''
