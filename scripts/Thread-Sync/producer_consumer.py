import threading
import queue
import random
from time import sleep

# This program demonstrates the classic producer-consumer problem and its synchronization using semaphores.

# Storyline: In the python Cafe, the waiter Bill places the order in the order queue
# and the chef Elon prepares the food order and clears the order queue.
# This is the classic example of producer-consumer problem with shared buffer resource.

# 'Python Cafe' Menu list.
cafe_menu = ['Sandwich',
             'French Fry',
             'Pizza',
             'Pasta',
             'Noodles',
             'Nuggets',
             'Ice Cream',
             'Fruit Juice',
             'Hot Coffee',
             'Cold Drinks']

# Order Buffer Size.
BUFFER_CAPACITY = 10

# Order Queue.
order_queue = queue.Queue(BUFFER_CAPACITY)

# Semaphores used.
empty_order = threading.Semaphore(BUFFER_CAPACITY)
full_order = threading.Semaphore(0)
mutex_order = threading.Semaphore()

# This fuction places the orders.


def place_order():
    global cafe_menu, order_queue
    name = threading.current_thread().name

    for _ in range(20):
        # Getting the locks.
        empty_order.acquire()
        mutex_order.acquire()

        # Critical Section.
        item = random.choice(cafe_menu)
        order_queue.put(item)
        print(f'{name} places order for {item}')

        # Release the locks.
        mutex_order.release()
        full_order.release()

        sleep(0.5)


# This function clears the orders.


def prepare_order():
    global order_queue
    name = threading.current_thread().name

    for _ in range(20):
        # Getting the locks.
        full_order.acquire()
        mutex_order.acquire()

        # Critical Section.
        item = order_queue.get()
        print(f'{name} processed the order for {item}')

        # Release the lock
        mutex_order.release()
        empty_order.release()

        sleep(1)

# This is the main function.


def python_cafe():
    print('\n************** Python Cafe Order Processing *****************\n')

    bill = threading.Thread(name='Bill', target=place_order)
    elon = threading.Thread(name='Elon', target=prepare_order)

    bill.start()
    elon.start()

    bill.join()
    elon.join()

    print('\nOrder Complete!\n')


if __name__ == '__main__':
    python_cafe()
