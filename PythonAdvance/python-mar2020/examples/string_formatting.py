name = 'Ana'
age = 20
height = 1.725

# f-strings
print(f'{name} is {age} years old and is {height}m tall.')
print(f'{len} is a built-in function')

# str.format() method
print('{} is {} years old and is {}m tall.'.format(name, age, height))
print('{0} is {1} years old and is {2}m tall. {0} is a student.'.format(name, age, height))
print('{name} is {age} years old and is {height}m tall. {name} is a student.'.format(
    name='Mihai', age=22, height=1.8))

person = {'name': 'Adina', 'age': 22, 'height': 1.7}
print('{name} is {age} years old and is {height}m tall. {name} is a student.'.format(**person))

# % formatting
print('%s is %d years old' % (name, age))

print(f'|{name:*^20}|{age:+5}|{height:5.3}')
