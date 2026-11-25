# FILE OPERATIONS 
''' the actions performed on files, such as creating , reading, writting , copy and deleting 
'''

# DIRECTORY OPERATORS
''' The actions performed on folders , such as creating , listing contents , renaming and , moving and deleting directors
'''

# PYTHON FILES AND DIRECTORY TOOLS 
''' OS - it provides features of opearting systems , like listing directory contents , creating folders 
'''
#creating directory and nested directory
#import os
#os.mkdir("my_directory",exist_ok=True)
#os.makedirs("parent_directory/child_directory",exist_ok=True)


#PATHLIB
# It provides object orriented way to work with file paths , we can build and check files , we cam read and write 

# WORKING WITH DIRECTORIES USING PATHLIB
from pathlib import Path
Path("my_new_dir").mkdir(exist_ok=True)
for file in Path(".").iterdir():
    print(file)
    
#SHUTIL
# It provides the higher level operations for copying , moving , and deleting files and directory tools 

#The below code copies al files , folders from src-dir into destination_dir

import shutil
shutil.copytree("abc.py", "destination_dir",dirs_exist_ok =True)
print("directory copied sucessfully")    




