import os


print(os.listdir('..'))
for dirpath, dirnames, filenames in os.walk('../pypackage'):
    print(dirpath, dirnames, filenames)

print(os.getcwd())

path = os.path.join('test_dir', 'inner_dir', 'file.txt')
print(path)
print(os.path.split(path))

print(os.path.dirname(path))
print(os.path.basename(path))

print(os.path.exists(path))
print(os.path.exists(os.getcwd()))
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))
