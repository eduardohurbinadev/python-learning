#Example of Exception Handling when the parameter of b is "0"
a = input("type a number:")
b = input("type another number:")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero")
