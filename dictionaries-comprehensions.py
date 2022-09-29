# Dictionary
# my_car_dictionary = {
#     'Ford': 'Mustang', # Key - Value
#     'Tesla': '3',
#     'Chevrolet': 'Impala',
# }

carList = [('Ford', 'Mustang'), ('Tesla', '3'), ('Chevrolet', 'Impala')]
print(type(carList))
cars = { item[0]: item[1] for item in carList }
print(cars)
print(type(cars))

cars = { key: item for key, item in carList }
print(f'modified cars (?): {cars}')

