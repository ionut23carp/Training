from multiprocessing import Process, current_process, active_children
import time
import random


def doubler(nr):
    """
    A doubling function that can be used by a process
    """
    # Time-consuming processing:
    x = 0
    for i in range(1000000):
        x += random.randint(1, 10)

    result = nr * 2
    # grab the name of the process that is calling our function
    proc_name = current_process().name
    print('{} doubled to {} by: {}'.format(number, result, proc_name))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    time0 = time.time()
    for number in numbers:
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    # proc = Process(target=doubler, name='Test', args=(2,))
    # proc.start()
    # procs.append(proc)

    # while active_children():
    #     pass
    for proc in procs:
        proc.join()

    time1 = time.time()
    print(f'Total execution time (parallel): {time1-time0:.10f}')

    time0 = time.time()

    for number in numbers:
        doubler(number)

    time1 = time.time()
    print(f'Total execution time (serial): {time1 - time0:.10f}')
