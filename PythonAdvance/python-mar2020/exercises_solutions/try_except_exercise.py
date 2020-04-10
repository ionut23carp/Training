while True:
    try:
        x = float(input("x = "))
        y = float(input("y = "))
        result = x / y
    except ValueError:
        print('Please enter numeric values')
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print(result)
        break
