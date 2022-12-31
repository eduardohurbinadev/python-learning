#Example of Exception Handling when the parameter of b is "0"
a = input("Type a number: ")
b = input("Type another number: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero")
    
#Write a program that asks the user to type a number, convert it to an integer, and print it.
#If you can't convert their input to an integer, print a message that says "Please type an integer.
user_input = input("Type a number: ")
try:
    int(user_input)
    print(user_input)
except:
    print("Please type an integer.")
