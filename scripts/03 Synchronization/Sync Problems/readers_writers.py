import threading
import random
from time import sleep

# This program demonstrates the readers-writers problem solution using semaphores.

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

# Semaphore used.
mutex = threading.Semaphore()
reader_mutex = threading.Semaphore()

# Stop program event.
stop_event = threading.Event()


def writer():
    global day_idx, stop_event

    # Get the thread name.
    name = threading.current_thread().name

    while not stop_event.is_set():
        # Update the shared data.
        mutex.acquire()
        day_idx = random.randint(0, 6)
        print(f'{name} is updating the calendar to {calendar_days[day_idx]}.')
        mutex.release()
        sleep(1)


def reader():
    global day_idx, stop_event, reader_count

    # Get the thread name.
    name = threading.current_thread().name

    while not stop_event.is_set():
        # Increase the readers count by one.
        reader_mutex.acquire()
        reader_count += 1
        if reader_count == 1:
            mutex.acquire()
        reader_mutex.release()

        # Read the shared data.
        today = calendar_days[day_idx]
        print(f'{name} is reading calendar as {today} | Readers Count - {reader_count}')

        # Decrease the readers count by one.
        reader_mutex.acquire()
        reader_count -= 1
        if reader_count == 0:
            mutex.release()
        reader_mutex.release()
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
