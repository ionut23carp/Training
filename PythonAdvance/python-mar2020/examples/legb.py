# Shadowing built-in names should be avoided
# list = [1, 2]

GLOBAL_VAR_1 = 100
GLOBAL_VAR_2 = 500


def func(param):
    print('--- Inside func() ---')

    # global access modifier => we are using the global GLOBAL_VAR
    # global access modifier also works for defining global variables outside of global scope
    global GLOBAL_VAR_1
    GLOBAL_VAR_1 = 111

    # Local variable for function func()
    local_var = 1
    print('Local variables of function func()', local_var, param)
    print('Global variables are visible from inside func()', GLOBAL_VAR_1, GLOBAL_VAR_2)

    # Local variable inner_func
    def inner_func(inner_param):
        print('-- Inside inner_func() --')

        # nonlocal access modifier => we are using the nonlocal local_var (from enclosing scope)
        # nonlocal access modifier cannot be used to define variables in outer scopes
        nonlocal local_var
        local_var = 222222

        print('Local variables of function inner_func()', inner_param)
        print('Nonlocal variables (enclosing scope) are visible from inside inner_func()', local_var, param)
        print('Global variables are visible from inside inner_func()', GLOBAL_VAR_1, GLOBAL_VAR_2)

        print('-- inner_func() execution ended --')

    inner_func(22)
    print('local_var inside func() after being modified by inner_fun()', local_var)

    print('--- func() execution ended ---')


func(2)
print('At global level we see global built-in variables', GLOBAL_VAR_1, GLOBAL_VAR_2, func, list)
