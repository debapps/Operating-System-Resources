import threading
import random
from readerwriterlock import rwlock
from time import sleep

# This program demonstrates the readers-writers problem solution using readerwriterlock module.

# Week days name.
calendar_days = ['Sunday',
                 'Monday',
                 'Tuesday',
                 'Wednesday',
                 'Thursday',
                 'Friday',
                 'Saturday']

# Day index
day_idx = 0

# Reders Count.
reader_count = 0

# Stop program event.
stop_event = threading.Event()

# Readers Writers lock.
lock = rwlock.RWLockFair()


def writer():
    global day_idx, stop_event

    # Get the thread name.
    name = threading.current_thread().name

    # Writers lock.
    wrt_mutex = lock.gen_wlock()

    while not stop_event.is_set():
        # Update the shared data.
        wrt_mutex.acquire()
        day_idx = random.randint(0, 6)
        print(f'{name} is updating the calendar to {calendar_days[day_idx]}.')
        wrt_mutex.release()
        sleep(1)


def reader():
    global day_idx, stop_event, reader_count

    # Get the thread name.
    name = threading.current_thread().name

    # Readers lock.
    rd_mutex = lock.gen_rlock()

    while not stop_event.is_set():
        rd_mutex.acquire()
        # Increase the readers count by one.
        reader_count += 1

        # Read the shared data.
        today = calendar_days[day_idx]
        print(f'{name} is reading calendar as {today} | Readers Count - {reader_count}')

        # Decrease the readers count by one.
        reader_count -= 1
        rd_mutex.release()
        sleep(0.5)


def main():
    print('\n************** Readers-Writers Problem *****************\n')

    # Creating Writers threads.
    for writer_idx in range(5):
        threading.Thread(name='Writer - ' + str(writer_idx + 1),
                         target=writer).start()

    # Creating Readers threads.
    for reader_idx in range(5):
        threading.Thread(name='Reader - ' + str(reader_idx + 1),
                         target=reader).start()

    # The Main process sleeps for 3 seconds.
    sleep(3)

    # The Main process raises the stop event.
    stop_event.set()


if __name__ == '__main__':
    main()
