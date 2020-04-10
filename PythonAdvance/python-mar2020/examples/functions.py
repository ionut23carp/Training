def function():
    """
    This is a docstring. You should describe function behavior here
    :return: None
    """
    pass


# function is an object
print(function.__doc__, function.__name__)

# call function
return_value = function()
print('A function without return statement returns', return_value)


# a is an required argument
# b is a optional argument (because it has a default value)
def diff_of_two_numbers(a, b=0):
    return a - b


diff = diff_of_two_numbers(10)
print(diff)

# Calling function with positional arguments
diff = diff_of_two_numbers(10, 2)
print(diff)

# Calling function with keyword arguments
diff = diff_of_two_numbers(b=2, a=10)
print(diff)
