# Storyline: There are two chefs, Bill and Elon, works on a cafe called 'Python Cafe'.
# Bill makes sandwich. Elon makes pizza. They share a single oven to make food simultaneously.
# There is a garbage man, Donald, who collects garbage in the kitchen when Bill and Elon are cooking.
# Once the cooking stops Donald also stops collecting garages.

# In a given time frame, check how much sandwiches and pizzas are made
# where Bill and Elon work concurrently.

# Assumptions:
# •	Time taken to make one sandwich: 0.5 seconds.
# •	Time taken to make one pizza: 0.85 seconds.

# Solution: We can see Bill and Elon are two threads of the parent process - 'Python Cafe'.
# We will create a daemon thread for Donald as he is the garbage collector.


from time import sleep
import threading

# 'Python Cafe' function.


def python_cafe():
    print('\n************ Python Cafe Kitchen *********************\n')

    # Creating a thread stop event.
    stop_event = threading.Event()

    # Create two threads: bill and elon. Create a daemon thread for Donald.
    bill = threading.Thread(name='Bill',
                            target=make_sandwich,
                            args=(stop_event,))
    elon = threading.Thread(name='Elon',
                            target=make_pizza,
                            args=(stop_event,))
    donald = threading.Thread(name='Donald', target=clean_oven, daemon=True)

    # Cafe head-cook (parent process) orders two threads to start cooking.
    bill.start()
    elon.start()

    # Cafe head-cook (parent process) orders donald to start cleanning oven.
    donald.start()

    # Cafe head-cook (parent process) sleeps for sometimes (10 seconds).
    sleep(10)

    # Cafe head-cook (parent process) orders to stop cooking.
    stop_event.set()

# This function makes sandwich.


def make_sandwich(stop_event):
    sandwitch_count = 0

    while not stop_event.is_set():
        sandwitch_count += 1
        print(f' {threading.current_thread().name} makes a sandwich.')
        sleep(0.5)

    message = f'\n{threading.current_thread().name} makes total {sandwitch_count} sandwiches.\n'
    print(message)

# This function makes pizza.


def make_pizza(stop_event):
    pizza_count = 0

    while not stop_event.is_set():
        pizza_count += 1
        print(f' {threading.current_thread().name} makes a pizza.')
        sleep(0.85)

    message = f'\n{threading.current_thread().name} makes total {pizza_count} pizzas.\n'
    print(message)

# This function cleans the oven.


def clean_oven():

    while True:
        print(f' {threading.current_thread().name} is cleaning the oven.')
        sleep(1)


if __name__ == '__main__':
    python_cafe()
