# The term exceptions means python lo default unna errors like value error, type error kakunda , mana project kosam maname oka errornames ni create cheyadam custom exception 
# EX: If there is less balance in bank acc ,if  we define a insuffiecnt balance error instead of value error , it makes easier to read

class InsufficientBalanceError(Exception):
    pass
balance = 2000
withdraw = 3000
try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough money in account")

    print("Withdrawal successful")
except InsufficientBalanceError as e:
    print(e)
#here we created a error name wantedly by using the RAISE KEYWORD


# NOTE
# If we create a exception , it will not executes automatically , we should use RAISE keyword and it is mandatory

#custom exception with try and expect
class AgeError(Exception):
    pass
try:
    age= 15
    if  age<18:
         raise AgeError("age should be must 18")
    print("You can vote ")
except AgeError as e:
    print(e)
        
#EXCEPTION HIERARCHY
# it means one exception inherits from another 
# Genrally,in python all python exceptions follows a hierarchy structure , 