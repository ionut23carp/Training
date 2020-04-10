import glob
import os.path
import re
import time
from multiprocessing.dummy import Pool as ThreadPool


def get_files(path, extension):
    pattern = os.path.join(path, '**', f'*.{extension}')
    return glob.glob(pattern, recursive=True)


def get_matches(args):
    pattern, filename = args

    matches = []
    with open(filename) as f:
        try:
            for line in f:
                matches.extend(re.findall(pattern, line))
        except:
            pass
    return matches


if __name__ == '__main__':
    root_path = '/usr/local/Cellar/python/3.7.5'

    start_time = time.time()

    filenames = get_files(root_path, 'py')
    all_matches = []
    for fn in filenames:
        all_matches.append(get_matches((r'class \w+', fn)))

    end_time = time.time()
    print(f'Total execution time (serial): {end_time - start_time:.10f}. Matches: {len(all_matches)}')

    start_time = time.time()

    pool = ThreadPool(20)

    filenames = get_files(root_path, 'py')

    args_tuples = [(r'class \w+', fn) for fn in filenames]
    all_matches_parallel = pool.map(get_matches, args_tuples)

    end_time = time.time()
    print(f'Total execution time (parallel): {end_time - start_time:.10f}. Matches: {len(all_matches_parallel)}')

    assert all_matches == all_matches_parallel
