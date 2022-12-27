#Practice Functions
#Algebraic Function
def f(x):
     return x*2
result = f(2)
print(result)
#Function named square that takes a number, n, as a parameter and returns that number squared
def square(n):
    return n ** 2 
result = square(2)
print(result)
#Function called print_string that accepts a string as a parameter and prints it.
def print_string(x):
    return x
x = print_string("Hello World")
print(x)
#Function with three required parameters and 2 optional parameters
#Example 1
def opt(a,b,c,d=2,e=3):
    return a + b + c + d + e
result = opt(1,2,3)
print(result)
#Expample 2
def opt(a,b,c,d=2,e=3):
    return a + b + c + d + e
result = opt(1,2,3,4,5)
print(result)




