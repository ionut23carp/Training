try:
    name = input('name = ')
    d = {}
    name = d['name']
    # raise ValueError
except KeyError as ex:
    print(type(ex), ex)
except ValueError:
    print('ValueError raised!')
else:
    print('No exception occurred')
finally:
    print('Runs every time (exception / no exception)')
