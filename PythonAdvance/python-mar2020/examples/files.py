f = open('person_class.py')

# Brings all file contents in memory
# f.read()
# f.readlines()

for line in f:
    print(line)

f.tell()
f.seek(0)

f.close()

with open('out.txt', 'wb') as f:
    f.write('Bună\n'.encode())
    f.write(b'Hello world')

