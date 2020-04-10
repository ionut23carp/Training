def func(*args, **kwargs):  # formal arguments
    print('args:', args)
    print('kwargs:', kwargs, end='\n\n')


func()
func(1, 2, 3)  # positional arguments are mapped to formal arguments by position
func(name='Ana', age=25)  # key-word arguments are mapped to formal arguments by name
func(1, 2, 3, name='Ana', age=25)


def print_clone(*args, **kwargs):
    print('Calling built-in print & forwarding arguments')
    print(*args, **kwargs)  # variable un-packing


print_clone(1, 2, 3, 4, sep=" ** ")


def func_with_all_types_of_arguments(name, age, *args, flag=True, **kwargs):
    print(name, age, args, flag, kwargs)


func_with_all_types_of_arguments('Ana', 10, flag=False)


list1 = (1, 2, 3, 4)
dict1 = {'hello': 2, 'there': 2, 'anybody': 1, 'flag': False}
func_with_all_types_of_arguments(*list1, **dict1)
func_with_all_types_of_arguments(1, 2, 3, 4, hello=2, there=2, anybody=1)
