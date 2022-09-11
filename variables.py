###########################
###      VARIABLES      ###
###########################

# Variables are used to store information to be referenced and manipulated in a computer program.
# They also provide a way of labeling data with a descriptive name,
# so our programs can be understood more clearly by the reader and ourselves.

# Declare variable: 🔍
# A variable declaration provides assurance to the compiler / interpreter
# that there exists a variable with the given *type* and *name* so that the compiler can proceed
# for further compilation without requiring the complete detail about the variable. It also works
# as a pointer in memory, to access it.

# Initialise variable: 🏁
# The first time a variable is assigned a value, it is said to be initialised.
# The = symbol is known as the assignment operator.

my_name = 'Eduardo'

# It's important to make sure we add descriptive names:

AKZ = 10 # this is not a very descriptive name, because it doesn't make sense what 'AKZ' is.
UPPER_CASE = 'UPPER_CASE'
lower_case = 'lower_case'
PascalCase = 'PascalCase'
camelCase = 'camelCase'

 # These are descriptive names because they describe correctly what the variables are referring to.
hypotenuse = 5
leg_1 = 3 # It's a convention to use (_) between words in variables, this is called snake case 🐍
leg_two = 4

# 2_les = 1 ❌ It is not possible to start a variable with a number ❌

# Once the variables are declared, they can be modified or reassigned, like so:
hypotenuse = 10
leg_1 = 6
leg_two = 8

print(hypotenuse)
print(leg_1)
print(leg_two)
