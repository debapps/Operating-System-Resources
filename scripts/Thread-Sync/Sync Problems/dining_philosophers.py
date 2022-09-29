import threading
from time import sleep

# List of Semaphores.
chopsticks = []
for i in range(5):
    chopsticks.append(threading.Semaphore())

# Stoping event.
stop_event = threading.Event()


def philosopher(id):
    # Get the pholosopher name.
    name = 'Pholosopher - ' + str(id)

    while not stop_event.is_set():
        think_big(name)

        left = id
        right = (id + 1) % 5

        if id == 4:
            chopsticks[right].acquire()
            chopsticks[left].acquire()
        else:
            chopsticks[left].acquire()
            chopsticks[right].acquire()

        eat_noodles(name)

        if id == 4:
            chopsticks[right].release()
            chopsticks[left].release()
        else:
            chopsticks[left].release()
            chopsticks[right].release()


def think_big(philosopher_name):
    print(f'{philosopher_name} is thinking ... hummm..!')
    sleep(1)


def eat_noodles(philosopher_name):
    print(f'{philosopher_name} is eating noodles ... yum yum!!')
    sleep(0.05)


def main():
    print('\n********************** Dining Philosopher Problem **********************\n')

    for idx in range(5):
        threading.Thread(target=philosopher, args=(idx,)).start()

    sleep(6)

    stop_event.set()


if __name__ == '__main__':
    main()
