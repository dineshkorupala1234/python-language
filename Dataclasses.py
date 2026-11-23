# DATACLASS - This is a special class which is created to store the data this is called dataclass ! 
# DEFAULT VALUE: this is used  when we dont provide any value , for ex : age =20 , this is taken as default value 
# FIELD() : It is used to set a set a special rule for a variable in clas
#  > DEFAULT_FACTORY : if we want to give a empty list=[] to define , but if we use defalut_factor it wll create a empty list for each object
#  > repr=false : when we want to print the secret data like passwords , this helps in hiding that data 
# FROZEN DATACLASS : if we define it with @dataclass(frozen=True), it can only reads the data clas


from dataclasses import dataclass ,field
@dataclass (frozen = True)
class student:
    name: str
    age : int = 18      # default value
    courses: list= field(default_factory=list)
student = student("Dinesh Kumar")
print(student)
