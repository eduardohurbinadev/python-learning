#Global scope (outside a function) global variables 
x = 1
y = 2
z = 3
def f():
    print(x)
    print(y)
    print(z)
f()

#Local scope (inside a function)
x = 1
y = 2
z = 3
def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)
f()

#Global variable inside a local scope
x = 100
def f():
    global x
    x += 1
    print(x)
f()
