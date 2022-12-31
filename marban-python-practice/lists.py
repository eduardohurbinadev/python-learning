#Two ways to create a list in python
#Example 1
fruit = list()
print(fruit)

#Example 2
fruit = ["Apple", "Orange", "Pear"]
print(fruit)

#Add an item to the list and place it last
fruit = ["Apple", "Orange", "Pear"]
fruit.append("Bannana")
print(fruit)

#List can store any data type
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

#Use iterable index (starting from 0) to retrieve from a container (list)
fruit = ["Apple", "Orange", "Pear"]
print(fruit[1])

#Containers are mutable (editable), replace an object inside a container referencing its index number (position)
colors = ["Blue", "Green", "Yellow"]
colors[2] = "Red"
print(colors)

#Remove last item in a list
colors = ["Blue", "Green", "Yellow"]
item = colors.pop()
print(item)
print(colors)

#Combine lists
colors = ["Blue", "Green", "Yellow"]
fruit = ["Apple", "Orange", "Pear"]
print(colors + fruit)#["Blue", "Green", "Yellow", "Apple", "Orange", "Pear"]

#Check if an item is in a list
colors = ["Blue", "Green", "Yellow"]
item = "green" in colors
print(item)

#Check if an item is not in a list
colors = ["Blue", "Green", "Yellow"]
item = "black" not in colors
print(item)#True

#Get the number of items in a list
colors = ["Blue", "Green", "Yellow"]
items = len(colors)
print(items)#3

#Game to guess a color
colors = ["Blue", "Green", "Yellow"]
guess = input("Guess a color: ")
if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
