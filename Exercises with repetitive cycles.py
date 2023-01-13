# Ex. 1

# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# a.)
# for car in range(len(cars)):
#     print(f'My favourite car is {cars[car]}.')
# b.)

# for car in cars:
#     print(f'My favourite car is {car}.')

# c.)

# car = 0
# while (car<len(cars)):
#      print(f'My favourite car is {cars[car]}.')
#      car += 1;

# Ex. 2

# first_car = cars[0]
# last_car = cars[len(cars) - 1]
# for car in range(1, len(cars)-1):
#     cars[car] = cars[car].upper()
# else:
#     print(cars)

# Ex. 3

# for car in cars:
#     if car == 'Mercedes':
#         print(f'I found your dream car {car} !')
#         break
#     else:
#         print(f'I found another car {car}, I was still searching.')

# Ex. 4

# for car in cars:
#     if car == 'Trabant':
#         continue
#     if car == 'Lastun':
#         continue
#     print(f'I present the car {car}, an excellent car.')

# Ex. 5

# old_car = []
# for car in range(len(cars)):
#     if cars[car] == 'Trabant':
#         old_car.append('Trabant')
#         cars[car] = 'Tesla'
#     if cars[car] == 'Lastun':
#         old_car.append('Lastun')
#         cars[car] = 'Tesla'
# print(f'The old models is: {old_car}')
# print(f'The new models is: {cars}')

# Ex. 6

# car_price = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# car_budget = 15000
# for key, value in car_price.items():
#     if value <= car_budget:
#         print(f'For budget of {car_budget} euros you can choose the car {key} for the price of {value}.')

# Ex. 7

# numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# lucky_number = []
# for x in numbers:
#     if x == 3:
#         lucky_number.append(x)
# print(f'My number 3 appear of {len(lucky_number)} times.')

# Ex. 8

# x = 0
# for y in numbers:
#     x += y
# print(x)

# Ex. 9
# for x in numbers:
#     x = sorted(numbers)[-1]
# print(x)

# Ex. 10

# for x in numbers:
#     print(-x)

# Ex. 11

# alt_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# even_numbers = []
# odd_numbers = []
# positive_numbers = []
# negative_numbers = []
# for x in alt_numbers:
#     if x % 2 == 0:
#         even_numbers.append(x)
#     else:
#         odd_numbers.append(x)
#     if x >= 0:
#         positive_numbers.append(x)
#     if x < 0:
#         negative_numbers.append(x)
# print(f'The list with even numbers is {even_numbers}.')
# print(f'The list with odd numbers is {odd_numbers}.')
# print(f'The list with positive numbers is {positive_numbers}.')
# print(f'The list with negative numbers is {negative_numbers}.')

# Ex. 12

# for i in range(len(alt_numbers)):
#     for j in range(0, len(alt_numbers) - i - 1):
#         if alt_numbers[j] > alt_numbers[j + 1]:
#             x = alt_numbers[j]
#             alt_numbers[j] = alt_numbers[j + 1]
#             alt_numbers[j + 1] = x
# print(f'Sorted List in Ascending Order:\n{alt_numbers}')

# Ex. 13

# import random
# secret_number = random.randint(1, 30)
# print(secret_number)
# guess = 1
#
# while guess != secret_number:
#     guess = int(input("Try to guess the number:\n"))
#     if guess > secret_number:
#         print("Wrong! You guessed too high")
#     if guess < secret_number:
#         print("Wrong! You guessed too low")
# else:
#     print("You got it!")

# Ex. 14

# rows = int(input(f'Please insert a number for your pyramid:\n'))
# print(f'Look at the pyramid !')
# for i in range(rows + 1):
#     for j in range(i):
#         print(i, end='')
#     print('')

# Ex. 15

# keyboard_phone = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for x in keyboard_phone:
#     for y in keyboard_phone[1]:
#         print(f'Current digit is {y}')
#     break

