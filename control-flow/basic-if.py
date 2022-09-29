import random
import time

# If statements
print('Hello! and welcome to this awesome game...')
time.sleep(3)
guess = int(input('Guess one number from 1 to 10: '))
expected_number = random.randint(1, 10)

if guess == expected_number:
    print('You got it right!')
else:
    print('Oops try again')
