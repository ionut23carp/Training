import threading
import time

total = 0
lock = threading.Lock()


def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    # lock.acquire()
    # try:
    #     for _ in range(1000000):
    #         total += amount
    # finally:
    #     lock.release()

    with lock:
        for _ in range(1000000):
            total += amount

        # Step 1: get total
        # Step 2: compute total + amount
        # Step 3: set total to new value (total + amount)

    print(total)
    time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for _ in range(10):
        my_thread = threading.Thread(target=update_total, args=(1,))
        my_thread.start()
        threads.append(my_thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print('Total', total)
    print(f'Total execution time: {end_time - start_time:.10f}')
