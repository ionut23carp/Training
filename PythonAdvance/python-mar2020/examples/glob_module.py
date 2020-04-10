import os
import glob


os.chdir('..')

for file in glob.glob('*/*.py'):
    print(file)

print()

for file in glob.iglob('**/*.py', recursive=True):
    print(file)
