import threading

# This program demonstrates the race condition of a shared resources by two threads.
# When a shared resource is updated by multiple concurrent threads/processes,
# then the final value of the shared resource become unpredictable. This situation is called
# the race condition.

# Storyline: The python cafe has two employees - Tom and Harry. Tom works as waiter takes live orders
# of sandwiches; Harry takes phone order of sandwiches. Both update the sandwich order count
# at a same time making a data race.

sandwich_order_count = 0


def take_order():
    global sandwich_order_count
    for _ in range(1000000):
        sandwich_order_count += 1


def main():
    tom = threading.Thread(target=take_order)
    harry = threading.Thread(target=take_order)

    tom.start()
    harry.start()

    tom.join()
    harry.join()

    print(f'\nTotal sandwich order count - {sandwich_order_count}\n')


if __name__ == '__main__':
    main()
