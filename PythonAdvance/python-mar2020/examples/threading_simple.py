import threading
import time


def func(nr):
    print("Thread no. {}".format(nr))
    time.sleep(3)
    print("Finished sleeping from thread {}".format(nr))


time_start = time.time()
threads = []

for i in range(1, 6):
    t = threading.Thread(target=func, args=(i, ))
    # target(*args) --> func(i)
    t.start()

    # check if the thread is alive
    status = t.isAlive()
    # fetch the name of the thread
    name = t.getName()
    print('Thread {} alive status: {}'.format(name, status))

    # get total number of threads in execution
    count = threading.active_count()
    print("Total no of threads: {}".format(count))

    threads.append(t)

for thread in threads:
    thread.join()

# while threading.active_count() > 1:
#     pass

time_end = time.time()
total_time = time_end - time_start
print(f'Total time: {total_time:.10f}')
