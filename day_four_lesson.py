# Creating variable called first_name 
first_name = "Adekola"

# Creating variable called last_name 
last_name = "Abdulhakeem"

# Printing out the name on a single line 
print(first_name, last_name)

# Creating a list called favourite_fruits
favourite_fruits = ["Apple","Banana","Mango"]

# Printing the first and the last fruit of the list 
print(favourite_fruits[0])
print(favourite_fruits[2])

# Replacing the second fruit in the list with another
favourite_fruits = ["Apple","Cherry","Mango"]

# Printing the list 
print(favourite_fruits)

# Creating a tuple that represent coordinates
coordinate = (20, 10, 30)

# Printing the first value of the tuple
print(coordinate[0])

# Creating a dictionary called my_profile 
my_profile = {
    "name": "Adekola Abdulhakeem",
    "age": 50,
    "city": "Lagos"
}

# Printing the name and city by accessing it with the keys 
print(my_profile["name"])
print(my_profile["city"])

#Adding a new key called hobby
my_profile = {
    "name": "Adekola Abdulhakeem",
    "age": 50,
    "city": "Lagos",
    "hobby": "Solving Problem"
}

# Printing the updated version of the dictionary
print(my_profile)

# Creatign a set called  unique_numbers
unique_numbers = { 1, 2, 3, 3, 4, 4, 5}

#Printing the set
print(unique_numbers)

#What happened: The set of nubers were printed without duplicate 