import threading
from time import sleep
import random

# This program demonstrates how concurrent threads are synchronized processing
# using the semaphore mechanism.

# Storyline: There is only one car charging socket in the 'Python Charging Station'
# where 10 electric cars {EMV} came for charging. Cars takes random time to fully charged. This program
# output describes the charging pattern of 10 EMVs in the 'Python Charging Station'.

# When there is 1 charging socket in the 'Python Charging Station'.
# charging_socket = threading.Semaphore()

# When there are 4 charging sockets in the 'Python Charging Station'.
charging_socket = threading.Semaphore(4)


def car_charger():
    name = threading.current_thread().name
    charging_socket.acquire()
    print(f'Now Charging - {name}')
    sleep(random.uniform(1, 2))
    print(f'{name} is completed charging.')
    charging_socket.release()


def python_charging_station():
    print('\n***************** Python Charging Station *******************\n')
    for car in range(1, 11):
        threading.Thread(name='Electric Car - ' + str(car),
                         target=car_charger).start()


if __name__ == '__main__':
    python_charging_station()
