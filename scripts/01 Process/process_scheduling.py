# This program demonstrates the scheduling of multiple processes.
from multiprocessing import Process
import os
import time

# This fuction displays the process information.


def get_info(title):
    print(f'\n****************** {title} *********************\n')
    print(f' Module name: {__name__}')
    print(f' Process id: {os.getpid()}')
    print(f' Parent process: {os.getppid()}')
    print(f'\n****************** {title} *********************\n')

# This function loops and increament.


def do_work(continue_flag):
    get_info(f'Function Work: PID - {os.getpid()}')
    work_counter = 0
    while continue_flag:
        work_counter += 1
        continue_flag -= 1
        print(f' Process - {os.getpid()} completes {work_counter} work(s).')
        time.sleep(1)
    print(
        f'\n*** Process - {os.getpid()} did total {work_counter} works! ***\n')

# The Main Function.
# start(): It starts the process to execute state.


def main():
    get_info(f'Function Main: PID - {os.getpid()}')

    # Spawning the processes.
    p1 = Process(target=do_work, args=(5,))
    p2 = Process(target=do_work, args=(3,))

    # Starting the processes for concurrent execution.
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
