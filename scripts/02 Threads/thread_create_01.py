# This process demonstrate the creation of multiple threads from a process.
# Thread is created by passing target function into the Thread object constructor.
import threading
import time

# Main Function: Thread is created by passing target function into the Thread object constructor.
# start(): This method is used to start the thread.


def main():
    t1 = threading.Thread(name='Thread-1', target=greeting, args=(10,))
    t2 = threading.Thread(name='Thread-2', target=greeting, args=(10,))
    t1.start()
    t2.start()

# This function greets in a loop with a delay.


def greeting(count):
    # Get the current thread object.
    thread_obj = threading.current_thread()
    # Display the thread name.
    for _ in range(count):
        print(f' Hello World, from Thread - {thread_obj.name}')
        time.sleep(0.06)


if __name__ == '__main__':
    main()
