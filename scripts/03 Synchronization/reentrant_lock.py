import threading

# This program demonstrates the race condition of a shared resources by two threads
# with introduction of re-entrant locks.
# When a shared resource is updated by multiple concurrent threads/processes,
# then the final value of the shared resource become unpredictable. This situation is called
# the race condition.
# Race Condition can be prevent by data lock.
# A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread.

# Storyline: The python cafe has three employees - Tom, Harry and Jim. Tom works as waiter takes live orders
# of sandwiches; Harry takes phone order of sandwiches. Jim takes French Fry orders.
# When there is sandwich order, the single unit of French Fry will be ordered in the combo deal.
# French Fries can be ordered separately as well.

sandwich_order_count = 0
french_fry_order_count = 0

# Reentrant lock.
order_lock = threading.RLock()


def update_fry_order():
    global french_fry_order_count

    # Acquire the lock.
    order_lock.acquire()

    french_fry_order_count += 1

    # Release the lock.
    order_lock.release()


def take_combo_order():
    global sandwich_order_count

    # Acquire the lock.
    order_lock.acquire()

    for _ in range(1_000_000):
        sandwich_order_count += 1
        update_fry_order()

    # Release the lock.
    order_lock.release()


def take_fry_order():
    for _ in range(1_000_000):
        update_fry_order()


def main():
    tom = threading.Thread(target=take_combo_order)
    harry = threading.Thread(target=take_combo_order)
    jim = threading.Thread(target=take_fry_order)

    tom.start()
    harry.start()
    jim.start()

    tom.join()
    harry.join()
    jim.join()

    print(f'\nTotal sandwich order count - {sandwich_order_count}')
    print(f'\nTotal french fry order count - {french_fry_order_count}\n')


if __name__ == '__main__':
    main()
