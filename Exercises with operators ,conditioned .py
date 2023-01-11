# Ex. 1
# import math

# x = int(input('Please chose an option to find out what is :\nAn "IF" or \nAn "ELSE"\nFor "IF" press 1\nFor "ELSE" press 2\n'))
# if x == 1:
#     print(f'An "IF" comes from english from "FLOW CONTROL" and this help us how to control the code')
# elif x == 2:
#     print(f'An "ELSE" comes from english from "FLOW CONTROL" and this help us to choose the option for the other option')
# else:
#     print(f'The option chosen by you is not valid, Please choose another option. ')

# Ex. 2

# x = int(input('Please insert a number : \n'))
# if x >= 0:
#     print(f'Your number is {x} and he is a natural number.')
# else:
#     print(f'Your number is {x} and he is not a natural number because is a negative number.')

# Ex. 3

# x = int(input('Please insert a number :\n'))
# if x == 0:
#     print(f'Your number is {x} and he is neutral number.')
# elif x > 0:
#     print(f'Your number is {x} and he is a positive number.')
# else:
#     print(f'Your number is {x} and he is a negative number.')

# Ex. 4

# x = int(input('Please insert a number for verification if he is content between -2 and 13 :\n'))
# if -2 <= x <= 13:
#     print(f'Your number is {x} and he is content between -2 and 13.')
# else:
#     print(f'Your number is {x} and he is not content between -2 and 13.')

# Ex. 5

# x = int(input('Please insert a number for variable X :\n'))
# y = int(input('Please insert a number for variable Y :\n'))
# z = x - y
# if z < 5:
#     print(f'The difference between X and Y is {z} and he smaller than 5.')
# elif z >= 5:
#     print(f'The difference between X and Y is {z} and he is equal or higher than 5')

# Ex. 6

# x = int(input('Please insert a number :\n'))
# if not(5 <= x <= 27):
#     print(f'Your number is {x} and is not included between 5 and 27.')
# else:
#     print(f'Tour number is {x} and is included between 5 and 27')

# Ex. 7

# x = int(input('Please insert a number for variable X :\n'))
# y = int(input('Please insert a number for variable y :\n'))
# if x == y:
#     print(f'Your numbers is {x,y} and they is equal')
# elif x > y:
#     print(f'Your number is {x} and he is greater than {y}.')
# else:
#     print(f'Your number is {y} and he is greater than {x}.')

# Ex. 8
# print(f'We have the following sides for triangle :')
# x = int(input(f'Please insert a value for side X \n'))
# y = int(input(f'Please insert a value for side Y \n'))
# z = int(input(f'Please insert a value for side Z \n'))
# if x == y == z:
#     print(f'We have an equilateral triangle.')
# elif x == y or y == z or z == x:
#     print(f'We have an isosceles triangle.')
# else:
#     print(f'We have an scale triangle.')

# Ex. 9

# x = str(input('Please insert a letter :\n'))
# if x == ('a','e','i','o','u'):
#     print(f'You entered a vowel\n{x}')
# elif (x.isdigit()):
#     print(f'You entered a invalid letter\n{x}\nPlease reintroduce a valid letter :\n')
# else:
#     print(f'You entered a consonant \n{x}')

# Ex. 10

# x = int(input('Please insert a note for student aptitude :\n'))
# if x == 9:
#     print(f'You got the grade:\n{str("A")}')
# elif x == 8:
#     print(f'You got the grade:\n{str("B")}')
# elif x == 7:
#     print(f'You got the grade:\n{str("C")}')
# elif x == 6:
#     print(f'You got the grade:\n{str("D")}')
# elif x == 5:
#     print(f'You got the grade:\n{str("E")}')
# elif 4 >= x >= 0:
#     print(f'You got the grade:\n{str("F")}')
# else:
#     print(f'You entered a invalid number.')

# Ex. 11

# x = int(input('Please insert a number :\n'))
# z = str(x)
# y = len(z)
# if z >= '4':
#     print(f'Your number is {z} and has minimum 4 digits .')
# else:
#     print(f'Your number is {z} and does not contain minimum 4 digits.')

# Ex. 12

# x = int(input('Please insert a number :\n'))
# z = str(x)
# y = len(z)
# assert y == 6
# print(f'You choise a correct number')

# Ex. 13

# x = int(input('Please insert a number :\n'))
# if x % 2 == 0:
#     print(f'You have an even number.')
# else:
#     print(f'You have an odd number.')

# Ex. 14

# x = int(input('Please insert a value for variable X :\n'))
# y = int(input('Please insert a value for variable Y :\n'))
# z = int(input('Please insert a value for variable Z :\n'))
# if x > y and x > z:
#     print(f'Variable X is the greater number.')
# elif y > x and y > z:
#     print(f'Variable Y is the greater number.')
# elif z > x and z > y:
#     print(f'Variable Z is the greater number.')
# else:
#     print(f'All variables are equals.')

# Ex. 15

# x = int(input('Please insert a value for angle X :\n'))
# y = int(input('Please insert a value for angle Y :\n'))
# z = int(input('Please insert a value for angle Z :\n'))
# if x + y > z or y + z > x > x and x + z > y:
#     print(f'Triangle is valid.')
# else:
#     print(f'Triangle is invalid.')

# Ex. 16

# y = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Please insert a number for you to read our string.\n'))
# if len(y) >= x >= 0:
#     print(f'{y[:-x]}')
# else:
#     print(f'Invalid number, please reintroduce another number to read our string :')

# Ex. 17

# x = 'Coral is either the stupidest animal or the smartest rock'
# y = (x[0:5] + x[-5::])
# print(f'{y}')

# Ex. 18

# x = 'Coral is either the stupidest animal or the smartest rock'
# print(f'{x[-4::]}')
# y = x[-4::]
# print(f'{x.strip(y)}')

# Ex. 19

# x = str(input('Please insert a string :\n'))
# first_character = x[0]
# last_character = x[-1]
# assert first_character.lower() == last_character.lower()
# print(f'The first character of your word is "{first_character}" and the last character of your word is
# "{last_character}" and these are the same.')

# Ex. 20

# x = '0123456789'
# print(f'{x[::2]}')
# print(f'{x[1::2]}')

# Ex. 21

# Test Case 1 :
# If the person has over 18 years, and she has passport.
# Expected result : Pass --> "You are allowed to board."

# Test Case 2 :
# If the person don't have over 18 years, and he has passport.
# Expected result : Failed --> "You are not allowed to board."

# Test Case 3 :
# If the person don't have over 18 years, and he doesn't have a passport.
# Expected result : Failed -->  "You are not allowed to board."

# Test Case 4 :
# If the person don't have over 18 years, and she has passport, and mother and father accompany the person.
# Expected result : Pass -->  "You are allowed to board."

# Test Case 5 :
# If the person don't have over 18 years, and she has passport, and only one of the parents accompanies the person.
# Expected result : Failed -->  "You are not allowed to board."

# Test Case 6 :
# If the person don't have over 18 years, and she has passport, and only one of the parents accompanies the person,
# and the parent who does not accompany him gives his consent.
# Expected result : Pass -->  "You are allowed to board."

# Test Case 7 :
# If the person don't have over 18 years, and she has passport, and only one of the parents accompanies the person,
# and the parent who does not accompany he does not agree.
# Expected result : Failed -->  "You are not allowed to board."

# Test Case 8 :
# If the person don't have over 18 years, and she has passport, and no parent accompanies him.
# Expected result : Failed -- > "You are not allowed to board."

# Test Case 9 :
# If the person don't have over 18 years, and she has passport, and no parent accompanies him,
# and the mother or father gives their consent.
# Expected result : Failed -- > "You are not allowed to board."


# print(f'Hello, welcome to fly number 3099.\n\nFor boarding please present the documents.\n')
# age = int(input('Please insert your age for trip validation :\n'))
# passport = str(input('Please answer "yes" or "no" if you have a passport\n'))
# with_mom = str(input('Please answer "yes" or "no" if your mother accompanies you if you are not 18 years old :\n'))
# with_dad = str(input('Please answer "yes" or "no" if your father accompanies you if you are not 18 years old :\n'))
# act_mom = str(
#     input('Please answer "yes" or "no" if your mother gives you permission to board if she is not present :\n'))
# act_dad = str(
#     input('Please answer "yes" or "no" if your father gives you permission to board if she is not present :\n'))
#
# if age > 18 and passport == "yes":
#     print(f'You are allowed to board.')
# elif with_mom and with_dad == "yes":
#     print()
#     if with_mom or with_dad == "yes" and act_mom or act_dad == "yes":
#         print(f'You are allowed to board.')
#     else:
#         print()
# else:
#     print(f'You are not allowed to board.')


#  Test Case 1 :
#  Actual Result : Pass -- > You are allowed to board.

#  Test Case 2 :
#  Actual Result : Pass -- > You are not allowed to board.

#  Test Case 3 :
#  Actual Result : Pass -- > You are not allowed to board.

#  Test Case 4 :
#  Actual Result : Pass -- > You are allowed to board.

#  Test Case 5 :
#  Actual Result : Pass -- > You are not allowed to board.

#  Test Case 6 :
#  Actual Result : Pass -- > You are allowed to board.

# Test Case 7 :
# Actual Result : Pass -- > You are not allowed to board

# Test Case 8 :
# Actual Result : Pass -- > You are not allowed to board

# Test Case 9 :
# Actual Result : Pass -- > You are not allowed to board

# Ex. 22

# import random
#
# print(
#     f'Welcome to dice game !\n\nThe game which can your victory.\n\nAll you have to do is choose a number and if the '
#     f'dice is that number you will be the big winner !\n')
# win_numbers = int(input('Please insert your lucky number :\n'))
# dice_roll = random.randint(0, 12)
#
# if 0 <= win_numbers <= 12 and win_numbers == dice_roll:
#     print(f'You guessed it\nCongrats !\nYou choose {win_numbers} and the dice was {dice_roll}')
# elif 0 <= win_numbers <= 12 and win_numbers > dice_roll:
#     print(f'You lose !\nYour choose a biggest number. Your number is {win_numbers} and the win number is {dice_roll}')
# elif 0 <= win_numbers <= 12 and win_numbers < dice_roll:
#     print(f'You lose !\nYour choose a smaller number. Your number is {win_numbers} and the win number is {dice_roll}')
# else:
#     print(f'You choose a wrong number,\nPlease choose another number to win !')
