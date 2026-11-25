# The term python package menagement is installing , updating and removing and reusing 
''' PIP 
Genrally , it is used to install packages , libraries , it allows user to easily download the packages from python package index
Basic syntax : pip <command>

BASIC PIP COMMANDS 
____________________________
pip--version          > to check the pip version 
pip install numpy     > to install numpy package
pip install==1.26.4   >to install the specific version 
pip show numpy        >to view package information 
pip list              >to see installed packages 
pip uninstall numpy   >to uninstall the package 
pip install --upgrade numpy  >to upgrade the package 
pip list--outdated    > to see the outdated package 

'''

#VIRTUAL ENVIRONMENT
# It is like a space , it keeps the pythons projects , packages seperately without combing with another projets
# TOOLS : venv , virtualenv
# NEED OF VIRTUAL ENVIRONMENT 
''' 1. helps in avoiding package conflits 
    2. makes easy to share packages 
    3. keeps each project package seperately 
'''


#REQUIREMENTS.TXT
# python lo manam use chese anni external libraries and vaati oka versions lists ni store chese oka text file 
# IMP COMMANDS
''' pip freeze >requirements.txt          -> to create file
    pip install -r requirements.txt       -> to install packages from file 
'''
