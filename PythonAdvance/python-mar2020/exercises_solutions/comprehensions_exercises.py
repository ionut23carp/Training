import string


d1 = {x: ord(x) for x in string.ascii_lowercase[:5]}
print(d1)

d2 = {v: k for k, v in d1.items()}
print(d2)

d3 = {k: v for k, v in d2.items() if k % 2 == 0}
print(d3)

d4 = {ord(x): x for x in string.ascii_lowercase[:5] if ord(x) % 2 == 0}
print(d4)

d4 = {v: k for k, v in d1.items() if v % 2 == 0}
print(d4)
