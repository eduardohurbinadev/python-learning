###########################
###        TYPES        ###
###########################

# Numbers
int_number = 3
print(type(int_number))
float_number = 3.14159265
print(type(float_number))
complex_number = 4 + 1j
print(type(complex_number))

# Strings
string = 'Hello'
print(type(string))

# Booleans
my_boolean = False
my_boolean_two = True

my_comparator = 4 > 5 # False

# Data Structures
# Sorting Algorithms
# Search Algorithms
# Shortest way Algorithms

# List (Arrays)
# Lists are dynamic
my_list = ["Volkswagen", "Ford", "Tesla"] # square brackets: []
# Prints using index
print(my_list)
print(my_list[1]) # Ford
my_list.append("Kia")
print(my_list)
my_list.pop()
my_list.pop()
print(my_list)
print(type(my_list))

# Tuple
my_tuple = ("S", "3", "X", "Y") # brackets: ()
print(type(my_tuple))
print(my_tuple)

# Range
print(list(range(10)))

# Dictionary
my_car_dictionary = {
    'Ford': 'Mustang', # Key - Value
    'Tesla': '3',
    'Chevrolet': 'Impala',
}

print(my_car_dictionary['Ford']) # Mustang
print(my_car_dictionary['Chevrolet']) # Impala
print(my_car_dictionary['NoExisto'])

# Set
my_set = { 1, 2, 3, 4, 5, 2, 3, 1 }
print(my_set)
