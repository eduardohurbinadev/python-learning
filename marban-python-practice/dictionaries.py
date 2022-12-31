#Dictionaries are used to link one object "key" to another object "value" this is called mapping
my_dict = {
    "Canada": "Ontario",
    "Japon": "Tokio",
    "Brazil": "Sao Paulo", 
    "Mexico": "Ciudad de Mexico"
} 
print(my_dict["Canada"])

#Add a new key to the dictionary
my_dict["USA"] = "Washington D.C."
print(my_dict)

#Modify a value
my_dict["USA"] = "Chicago"
print(my_dict)

#Remove a key
my_dict.pop("Brazil")
print(my_dict)