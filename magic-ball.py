import random

result = random.randint(0, 2)

if result == 0:
    print('Yes! Absolutely!')
elif result == 1:
    print('No way!')
else:
    print('Hmm... maybe')

lucky_number = random.randint(1, 100)

print(f"Today you'll have a nice day! Your Lucky Number is {lucky_number}")
