x = 1235

last_digit = str(x)[-1]
print(last_digit)

# It is better to use arithmetic operations on numbers than cast to string and do string operations
last_digit = x % 10
print(last_digit)


x = 317

sum_of_digits = x % 10 + x // 10 % 10 + x // 100
print(sum_of_digits)


n = 150
hours_passed = n // 60
minutes_passed = n % 60
print(hours_passed, minutes_passed, sep=':')

print(*divmod(n, 60),  sep=':')
