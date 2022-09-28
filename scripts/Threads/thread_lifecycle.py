# This program demonstrates the thread life cycle. Threads have following states in general:
# 1. New 2. Executing/Running 3. Blocked 4. Terminated.

# Storyline: Donald is the kitchen cleaner of the 'Python Cafe' on demand.
# He is called by the 'Python Cafe' head-cook and cleans the kitchen.
# He waits for 4 seconds to prepare for his cleanning tools. Once the Cafe is closed,
# the head-cooks orders Donalds to stop cleaning.


import threading
from time import sleep


def python_cafe():
    print('\n*********************** Python Cafe ******************************\n')

    # Creating the kitchen cleaner thread.
    donald = threading.Thread(name='Donald', target=clean_kitchen)
    print(f'Head-cook appoints (creates) kitchen cleaner - {donald.name}')
    print(f' Is {donald.name} working? {donald.is_alive()}')
    print(f'* New State *')

    # Asking the Donald to start work.
    print(f'\nHead-cook orders {donald.name} to start working.')
    donald.start()
    print(
        f' Is {donald.name} working? {donald.is_alive()}\n* Runnable/Executing State *')

    # Head-cook sleeps for 1 seconds.
    print('\nHead-cook sleeps for 1 seconds....')
    sleep(1)

    print('\nHead-cooks checks if Donald is still working?')
    print(
        f' Is {donald.name} working? {donald.is_alive()}\n* Runnable/Executing State *')

    # Head-cook waits for Donald utill he cleans the the kitchen.
    donald.join()
    print(f' Is {donald.name} working? {donald.is_alive()}')
    print(f'* Terminated State *')

    print('\n******* Python Cafe is closed now *******\n')

# This function cleans the kitchen.


def clean_kitchen():
    print(f' {threading.current_thread().name} is started cleaning the kitchen...')
    print(f'\n {threading.current_thread().name} waits for 4 seconds to prepare for his cleaning tools.\n* Blocked State *')
    sleep(4)
    print(f' \n{threading.current_thread().name} completed cleaning the kitchen!!\n')


if __name__ == '__main__':
    python_cafe()
