# Ex. 1


# def gathering_number(a, b):
#     sum = a + b
#     return sum
#
#
# print(gathering_number(5, 3))
# print(gathering_number(110, 66))

# Ex. 2


# def even_odd_number(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(even_odd_number(4))
# print(even_odd_number(13))

# Ex. 3


# def name_complet(first_name, last_name, middle_name):
#     sum = len(first_name) + len(last_name) + len(middle_name)
#     return sum
#
#
# print(name_complet("Mihai", "Ilut", "Vasile"))
# print(name_complet("Alin", "Tanase", "Gicu"))


# Ex. 4

# def area_rectangle(L, l):
#     area = L * l
#     return area


# print(area_rectangle(10, 5))


# Ex. 5


# def area_circle(R):
#     A = 3.14 * R**2
#     return A


# print(area_circle(4))
# print(area_circle(12))


# Ex. 6

# character = input(f'Please insert a character to verification appear in string :\n')
#
#
# def return_character(string):
#     if character in string:
#         return True
#     else:
#         return False
#
#
# print(return_character('alinus'))
# print(return_character('Cacao'))


# Ex. 7

# def count_letters(string):
#     count1 = 0
#     count2 = 0
#     for x in string:
#         if x.isupper():
#             count1 += 1
#         if x.lower():
#             count2 += 1
#     print(f'Numbers of upper characters is {count1}')
#     print(f'Numbers of lower characters is {count2}')
#
#
# count_letters('THIS is a Sample Text')

# Ex. 8


# def numbers_positive(list1, list2):
#     list1 = [i for i in list1 if i >= 0]
#     list2 = [i for i in list2 if i >= 0]
#     return list1, list2
#
#
# print(numbers_positive(list2=[2, -3, 55, -1, 53, 90, 4, 10, -45, -8], list1=[3, 45, 6, -8, -99, 8, -3, 44]))


# Ex. 9


# def no_return(x, y):
#     if x > y:
#         print(f'First number {x} is greater than second number {y}.')
#     elif y > x:
#         print(f'The second number {y} is greater than first number {x}.')
#     elif x == y:
#         print(f'The numbers is equal.')
#
#
# no_return(66, 69)
# no_return(88, 2)


# Ex. 10


# def optimus_function(a, numbers=None):
#     if numbers is None:
#         numbers = {}
#     if a not in numbers:
#         numbers.add(a)
#         print(f'I added the new number {a} in set.')
#         return True
#     elif a in numbers:
#         print(f'I not added the new number {a} in set {numbers} because it is already exists. ')
#         return False
#
#
# optimus_function(9, numbers={3, 2, 4, 5, 6, 7, 8})
# optimus_function(33, numbers={34, 22, 45, 5, 6, 17, 28, 33})


# Ex. 11


# def month(month):
#     if month == 'January' or 'March' or 'May' or 'Julie' or 'August' or 'October' or 'December':
#         return 31
#     if month == 'April' or 'June' or 'September' or 'November':
#         return 30
#     if month == 'February':
#         return 28


# print(month('March'))


# month_days_list = [('January', [31]), ('February', [28, 29]), ('March', [31]),
#                    ('April', [30]), ('May', [31]), ('June', [30]), ('Julie', [31]),
#                    ('August', [31]), ('September', [30]), ('October', [31]), ('November', [30]), ('December', [31])]
#
#
# def month_days(month):
#     for m, d in month_days_list:
#         if m == month:
#             return d[0]
#
#
# print(month_days('February'))
# print(month_days('September'))


# Ex. 12


# def calculator(x, y, z, w):
#     a = (x + y), (z + w)
#     print(f'The sum is {a}')
#     b = (x - y), (z - w)
#     print(f'The decreased is {b}')
#     c = (x * y), (z * w)
#     print(f'The multiplication is {c}')
#     d = (x / y), (z / w)
#     print(f'The division is {d}')
#     return a, b, c, d
#
#
# calculator(12, 3, 15, 5)
# calculator(40, 5, 33, 29)


# Ex. 13


# def dict_list(list1=None):
#     if list1 is None:
#         list1 = []
#     count = list1.count(0)
#     dict = {0: count}
#     count = list1.count(1)
#     dict.update({1: count})
#     count = list1.count(2)
#     dict.update({2: count})
#     count = list1.count(3)
#     dict.update({3: count})
#     count = list1.count(4)
#     dict.update({4: count})
#     count = list1.count(5)
#     dict.update({5: count})
#     count = list1.count(6)
#     dict.update({6: count})
#     count = list1.count(7)
#     dict.update({7: count})
#     count = list1.count(8)
#     dict.update({8: count})
#     count = list1.count(9)
#     dict.update({9: count})
#     [print(key, ':', value) for key, value in dict.items()]
#     return dict
#
#
# dict_list(list1=[1, 3, 1, 5, 9, 7, 7, 5, 5])
# dict_list(list1=[0, 3, 2, 5, 9, 6, 7, 4, 5, 3, 8])


# Ex. 14


# def three_num(a, b, c):
#     return max(a, b, c)
#
#
# print(three_num(2, 222, 8))


# Ex. 15


# def sum_of_number(a):
#     sum1 = 0
#     for i in range(0, a + 1):
#         sum1 += i
#     return sum1
#
#
# print(sum_of_number(4))
# print(sum_of_number(18))


# Ex. 16


# def common_numbers(list1, list2):
#     difference = list1.intersection(list2)
#     return difference
#
#
# print(common_numbers(list1={1, 1, 2, 3}, list2={2, 2, 3, 4}))
# print(common_numbers(list1={1, 31, 22, 3, 44}, list2={2, 22, 23, 44, 11, 1}))


# Ex. 17

# discount = int(input(f'Please insert wish your discount :\n'))
#
#
# def sales_days(price):
#     x = discount * price / 100
#     price_after_discount = price - x
#     if discount > 100:
#         print(f'invalid discount')
#     return int(price_after_discount)
#
#
# print(sales_days(100))
# print(sales_days(1030))


# Ex. 18

# from datetime import datetime
# import pytz
#
#
# def country_time(country):
#     country_time_zone = pytz.timezone(country)
#     country_time = datetime.now(country_time_zone)
#     print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
#
#
# country_time('Europe/Bucharest')
# country_time('Asia/Shanghai')


# Ex. 19
# from datetime import *
#
#
# def my_birthday():
#     today = date.today()
#     my_birthday = date(2023, 3, 3)
#     days_left = (my_birthday - today).days
#     print(str(days_left) + " days left until my birthday!")
#
#
# my_birthday()
