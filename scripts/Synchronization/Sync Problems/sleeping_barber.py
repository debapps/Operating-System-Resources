import threading
from time import sleep

# This program demonstrates the sleeping barber problem with semaphores.
# Storyline: There is a 'Python Barber Shop' where Charlie is the Barber who sleeps all the day on his
# chair when there is no customer in the shop. The shop has N number of waiting chairs, where the customers
# waits for the barber Charlie when he is busy with cutting hair of a customer. The customer needs to
# wake up Charlie when he is sleeping. If a new customer does not get a waiting chair for waiting, he
# leaves the barber shop.

# Maximum waiting capacity and waiting list.
MAX_CAPACITY = 5
waiting_queue = []
available_chairs = MAX_CAPACITY

# Semaphores.
cust_mutex = threading.Semaphore(0)
barber_mutex = threading.Semaphore(0)
chair_mutex = threading.Semaphore(1)

# Shop Close Event.
shop_close = threading.Event()


def barber_thread():
    global MAX_CAPACITY, waiting_queue, available_chairs, shop_close

    # Get the name of the thread.
    barber_name = threading.current_thread().name

    print(f'{barber_name} opens the Python Barber Shop at morning...')

    while not shop_close.is_set():
        if len(waiting_queue) == 0:
            print(f'{barber_name} is waiting for customer and sleeping ... zzzz!')
        else:
            cust_mutex.acquire()
            chair_mutex.acquire()
            customer = waiting_queue.pop(0)
            available_chairs = MAX_CAPACITY - len(waiting_queue)
            chair_mutex.release()
            barber_mutex.release()
            cut_hair(barber_name, customer)


def cut_hair(barber_name, customer):
    print(f'\n {barber_name} cuts the hair of {customer}. Cling Cling!\n')
    print(
        f'\n Waiting Queue: {waiting_queue}\n Available Chairs: {available_chairs}\n')
    sleep(2)


def customer_thread():
    global MAX_CAPACITY, waiting_queue, available_chairs

    # Get the name of the thread.
    cust_name = threading.current_thread().name
    print(f'{cust_name} enters the shop.. knock knock!')

    while True:
        chair_mutex.acquire()
        if available_chairs > 0:
            waiting_queue.append(cust_name)
            available_chairs = MAX_CAPACITY - len(waiting_queue)
            print(
                f'\n Waiting Queue: {waiting_queue}\n Available Chairs: {available_chairs}\n')
            chair_mutex.release()
            cust_mutex.release()
            barber_mutex.acquire()
            get_hair_cut(cust_name)
            break
        else:
            chair_mutex.release()
            leave(cust_name)
            break


def get_hair_cut(customer):
    print(f'\n {customer} gets haircut.. Great!')


def leave(customer):
    print(f'{customer} is leaving as the waiting queue is full. Better luck next time..')


def python_barber_shop():
    print('\n**************** Python Barber Shop *****************\n')

    # Create and start barber thread.
    charlie = threading.Thread(name='Barber - Charlie', target=barber_thread)
    charlie.start()

    # Create and start 10 customer threads.
    customers = []
    for idx in range(10):
        customers.append(threading.Thread(
            name='Customer - ' + str(idx + 1), target=customer_thread))

    for cust in customers:
        cust.start()

    sleep(0.5)
    print('\nThere is no other incoming customers for the day...')

    for cust in customers:
        cust.join()

    sleep(0.5)
    # Close the shop
    shop_close.set()

    print('\n Python Barber Shop is Closed Now!\n')


if __name__ == '__main__':
    python_barber_shop()
