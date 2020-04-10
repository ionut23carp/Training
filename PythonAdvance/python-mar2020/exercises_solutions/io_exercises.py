import glob
import os
import subprocess


def get_filenames(path, extension):
    file_pattern = f'*.{extension}'
    path_pattern = os.path.join(path, file_pattern)
    filenames = []
    for filepath in glob.glob(path_pattern):
        if not os.path.isfile(filepath):
            continue
        filenames.append(os.path.split(filepath)[1])
    return filenames


def get_filenames_gen(path, extension):
    file_pattern = f'*.{extension}'
    path_pattern = os.path.join(path, file_pattern)
    for filepath in glob.iglob(path_pattern):
        if not os.path.isfile(filepath):
            continue
        yield os.path.split(filepath)[1]



def ping_localhost():
    ping_command = 'ping -c 4 localhost'.split()
    with open('ping.txt', 'wb') as f:
        subprocess.run(ping_command, stdout=f)


if __name__ == '__main__':
    filenames = get_filenames(os.getcwd(), 'py')
    print(filenames)

    filenames = get_filenames_gen(os.getcwd(), 'py')
    print(filenames)
    for filename in filenames:
        print(filename)

    ping_localhost()
