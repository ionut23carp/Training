# 1
def count_lines(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count


def append_text(filename, text):
    with open(filename, mode='a+') as f:
        f.write(text)
        f.seek(0)
        for line in f:
            print(line, end='')


# 3
def grep(text, filename):
    with open(filename) as f:
        return [line for line in f if text in line]


def grep_gen(text, filename):
    with open(filename) as f:
        for line in f:
            if text in line:
                yield line

# 4
def grepinto(text, infile, outfile):
    with open(infile, 'r') as fin, open(outfile, 'w') as fout:
        for line in fin:
            if text in line:
                fout.write(line.lstrip())


if __name__ == '__main__':
    count_lines('oop_advanced_exercises.py')
    # Remove this `pass` from `oop_advanced_exercises.py` after executing this script
    append_text('oop_advanced_exercises.py', '    pass\n')

    res = grep('class', 'oop_advanced_exercises.py')  # res is list
    for matching_line in res:
        print(matching_line)

    res = grep_gen('class', 'oop_advanced_exercises.py')  # res is iterator
    for matching_line in res:
        print(matching_line)

    grepinto('class', 'oop_advanced_exercises.py', 'class.txt')

