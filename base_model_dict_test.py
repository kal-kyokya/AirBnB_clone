#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print("\n",my_model, "\n")
print(type(my_model.created_at))

print("-" * 50)

my_model_json = my_model.to_dict()
print("\n",my_model_json, "\n")

print("JSON of my_model")
for key in my_model_json.keys():
    print(
        f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")

print("-" * 50)

my_new_model = BaseModel(**my_model_json)

print(my_new_model.id)
print("\n",my_new_model, "\n")
print(type(my_new_model.created_at))

print("-" * 50)

print(my_model is my_new_model)
