# This program demonstrates the spawning of a process using python multiprocessing modules.
from multiprocessing import Process
import os
import time

# The Main Function.
# start(): It starts the process to execute state.


def main():
    get_info('Function Main')
    p1 = Process(target=delay_work, args=(10,))
    p1.start()

# This function displays the process information.


def get_info(title):
    print(f'\n****************** {title} *********************\n')
    print(f' Module name: {__name__}')
    print(f' Process id: {os.getpid()}')
    print(f' Parent process: {os.getppid()}')

# This function induced delay for sepcified second in time.


def delay_work(seconds):
    get_info('Function Delay Work')
    for sec in range(seconds):
        print('*** I am working ***')
        time.sleep(1)
    print('\n*** I am done! ***\n')


if __name__ == '__main__':
    main()
