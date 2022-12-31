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
fruit[0]
fruit[1]
fruit[2]
print(fruit)

#Containers are mutable (editable), replace an object inside a container referencing its index number (position)
colors = ["blue", "green", "yellow"]
colors[2] = "red"
print(colors)

#Remove last item in a list
colors = ["blue", "green", "yellow"]
item = colors.pop()
print(item)
print(colors)

#Combine lists
colors = ["blue", "green", "yellow"]
fruit = ["Apple", "Orange", "Pear"]
print(colors + fruit)

#Check if an item is in a list
colors = ["blue", "green", "yellow"]
item = "green" in colors
print(item)

#Check if an item is not in a list
colors = ["blue", "green", "yellow"]
item = "black" not in colors
print(item)

#Get the number of items in a list
colors = ["blue", "green", "yellow"]
items = len(colors)
print(items)

#Game to guess a color
colors = ["blue", "green", "yellow"]
guess = input("Guess a color: ")
if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
