#The Pydantic library in Python is used for data validation and data parsing using Python type hint.

#A Pydantic model is a Python class that defines the structure of your data using type hints. 
#It automatically checks and converts input values to the correct types.

#import the Pydantic base class
from pydantic import BaseModel,field_validator,model_validator,EmailStr,validator

#define a typed data model
class UserProfile(BaseModel):
    name : str
    surname : str = "Jadav" #default
    #Pydantic lets you set default values for fields and mark others as required
    age : int 
    email : EmailStr
    is_active: bool=True
    account_id: int

    @field_validator('age') 
    def check_age(cls,value): #cls is or class itself
        if value<18:
            raise ValueError('Age must be atleast 18')
        return value
    
    @validator('account_id')
    def check_id(cls,value):
        if value<=0:
            raise ValueError("Account no. can't be negative")
        return value
        

user=UserProfile(name="Khushi",age=21,email="khushi123@gmail.com",account_id=1)#"21" string will auto converted into int
print(user)
print(type(user.age))
print('\n')

#updating attribute
#Pydantic still keeps validation in place when you modify values.
user.name="khushbu"
print(user.name)
print('\n')

#this will convert data into json format
user_json_str=user.json()
print(user_json_str)
print('\n')

#this will convert json into pydantic format
# py_str=user.parse_raw(user_json_str)

#Model validators let you define validation rules that involve multiple fields or the model as a whole

# class User2(BaseModel):
#     password:str
#     confirm_password:str

#     #Runs validation after the model is fully initialized.
#     @model_validator(mode='after')
#     def passwords_match(cls,model):
#         if model.password!=model.confirm_password:
#             raise ValueError("Passwords do not match")
#         return model
    

# User2(password="k",confirm_password="k")

class type_hints(BaseModel):
    tags: list[str] = ["python","pydantic","fastapi"]
    quantities: list[int] = [1,5,2,3]
    word_counts: dict[str,int]={"month":6,"date":6}
    settings: dict[str,str]={"theme":"dark","language":"en"}

hint=type_hints()
print(hint)