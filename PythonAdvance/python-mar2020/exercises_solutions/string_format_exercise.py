persons = [
    {'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
    {'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
    {'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
]

print('-' * 35)

for person in persons:
    print('| {last_name:<15} {first_name:.1}. | {net_worth:>+10.2f} |'.format(**person))

    # print('| {0:<15} {1:.1}. | {2:>+10.2f} |'.format(person['last_name'], person['first_name'], person['net_worth']))
    # print(f'| {person["last_name"]:<15} {person["first_name"]:.1}. | {person["net_worth"]:>+10.2f} |')

    # fname = person['first_name']
    # lname = person['last_name']
    # nworth = person['net_worth']
    # print(f'| {lname:<15} {fname:.1}. | {nworth:>+10.2f} |')


print('-' * 35)
