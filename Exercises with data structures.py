# Ex. 1

# a.)
# musical_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(musical_notes)
# b.)
# musical_notes = musical_notes[::-1]
# c.)
# print(musical_notes)
# d.)
# musical_notes.sort(reverse=True) -- with this method return it to me in alphabetic order, not the initial list.
# musical_notes = musical_notes[::-1]
# e.)
# print(musical_notes)
# Ex. 2

# count_do = musical_notes.count('do')
# print(count_do)

# Ex. 3

value = 5
def func():
    value = 15
    print(value)
func()
print(value)


# Ex. 4

# list3.sort()
# print(list3)
# list3.pop(0)
# print(list3)

# Ex. 5

# if len(list3) == 0:
#     print(f'The list is empty .')
# else:
#     print(f'The list is not empty .')

# Ex. 6

# list3.clear()
# print(list3)

# Ex. 7

# if len(list3) == 0:
#     print(f'The list is empty .')
# else:
#     print(f'The list is not empty .')

# Ex. 8

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# keys = dict1.keys()
# print(keys)

# Ex. 9

# x = list(dict1)

# print(f'{x[0]} took note {dict1["Ana"]}.')
# print(f'{x[1]} took note {dict1["Gigel"]}.')
# print(f'{x[2]} took note {dict1["Dorel"]}.')

# Ex. 10

# dict1.update({'Dorel': 6})
# print(f'{x[2]} took note {dict1["Dorel"]} after contestation.')

# Ex. 11

# dict1.pop('Gigel')
#
# dict1.update({'Ionica': 9})
#
# print(f'They are new students :{dict1.keys()}')

#                      OR
# x = list(dict1)
# print(f'They are new students :{x}')

# Ex. 12

# days_of_the_week = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
# weekend = {'saturday', 'sunday'}

# days_of_the_week = list(days_of_the_week)
# days_of_the_week.append('monday')
# print(days_of_the_week)

# Ex. 13

# if weekend.issubset(days_of_the_week):
#     print(f'Weekend is a subset to days of the week.')
# else:
#     print(f'Weekend is not a subset to days of the week.')

# Ex. 14

# difference = days_of_the_week.difference(weekend)
# print(difference)

# Ex. 15

# difference = days_of_the_week.intersection(weekend)
# print(difference)

# Ex. 16

# list_players = ['Messi', 'Ronaldo', 'Mbappe', 'Neymar', 'Haaland']
# max_changes = 3
# changes_made = 0
# if 'Messi' in list_players and changes_made < max_changes:
#     list_players.remove('Messi')
#     player_out = 'Messi'
#     list_players.append('Hazard')
#     entered_player = 'Hazard'
#     print(f'Entered now {entered_player} and he left the field {player_out}, and you have {max_changes - changes_made} changes.')
# elif 'Messi' not in list_players:
#     player_out = 'Messi'
#     print(f'We are not making the change for {player_out} player is not on the field.')
#     print(f'You have {max_changes - changes_made} more changes.')
# else:
#     print(f'We are not making the change for you have no more available changes.')
