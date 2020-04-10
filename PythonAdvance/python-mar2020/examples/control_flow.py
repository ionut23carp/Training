x = 10

while x > 0:
    print(x)
    if x == 6:
        break
    x -= 2
else:
    print('else branch!')


for char in 'good morning':
    print(char)


for nr in range(1, 10, 3):
    print(nr)
else:
    print('nr', nr)


for nr in range(20):
    if nr % 3 == 0:
        continue
    print(nr)


for x in range(100):
    pass
