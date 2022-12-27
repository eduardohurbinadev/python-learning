#Returns leght of an object
print(len("Python"))
#Return an object into a string
str(100)
#Takes a float or a string with a number in it and returns an integer object
int("1")
#Takes an integer or a string with a number in it and returns a floating point number object
float(100)
#input collects information from the person using the program
age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
if int_age > 21:
    print("Wow, you are old!")