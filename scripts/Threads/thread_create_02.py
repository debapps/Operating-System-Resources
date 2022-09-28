# This process demonstrate the creation of multiple threads from a process.
# Thread is created by overriding run() method in the subclass of Thread class.
import threading
import time


# Thread is created by overriding run() method in the subclass of Thread class.


class GreetThread(threading.Thread):
    def __init__(self, name, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        # Display the thread name.
        for _ in range(self.count):
            print(f' Hello World, from Thread - {self.name}')
            time.sleep(0.06)

# Main Function:
# start(): This method is used to start the thread.


def main():
    t1 = GreetThread('Thread-1', 10)
    t2 = GreetThread('Thread-2', 10)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
