s = 'bandana'

# While we can use find() method to check if a substring is contained in a string,
# this method gives us more info than we need (the position of the substring in the string)
if s.find('and'):
    print('Yes!')

# Using "in" operator does exactly what we need
if 'and' in s:
    print('"and" is contained in', s)

# Do not use special methods directly like this:
str.__contains__(s, 'and')
s.__contains__('and')

# There are two methods to find the index of a substring in a string
# They do slightly different things (raising an error if the substring is not found vs returning -1)
s.index('n')
s.find('q')

print(s.count('an'))

# Checking if a string is alphanumeric
s.isalnum()

# Transforming a string to all uppercase
# This method returnis the modified string, leaving the initial string unaltered, because strings are immutable
upper_s = s.upper()
