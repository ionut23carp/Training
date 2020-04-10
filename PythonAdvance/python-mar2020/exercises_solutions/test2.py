import threading
import os
import re


def funrt(ext, location):
    return [f for f in os.listdir(location) if f.endswith(ext)]


def find2(patt, filename):
    res = []
    with open(filename) as f:
        for lin  in f:
            res.extend(re.findall(patt, lin))
    return res

print(funrt(".py", "/home/ionut/Documents/PythonAdvance/python-mar2020/exercises_solutions"))
print([find2("import", fis) for fis in funrt(".py", "/home/ionut/Documents/PythonAdvance/python-mar2020/exercises_solutions")])


