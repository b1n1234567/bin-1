car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
y = car.values()
print(y)
car["color"] = "white"
print(x) #after the change

#update a value
car["year"] = 2020
print(y)

# See the list 
z = car.items()
print(z)

# Check if "model" is present in the dictionary
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")