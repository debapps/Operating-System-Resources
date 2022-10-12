import time
import threading

# Global Variables.
square_list = []
cube_list = []

# This function calculates the square of a list of numbers and put them in global variables.
# It induces 0.5 seconds delay in each calculation to simulate the I/O overhead.


def calculate_square(number_list):
    global square_list
    for num in number_list:
        print('  Calculating square ...')
        square_list.append(num * num)
        time.sleep(0.5)

# This function calculates the cubes of a list of numbers and put them in global variables.
# It induces 0.5 seconds delay in the each calculation to simulate the I/O overhead.


def calculate_cube(number_list):
    global cube_list
    for num in number_list:
        print('  Calculating cube ...')
        cube_list.append(num * num * num)
        time.sleep(0.5)


def main():
    print('\n****************** Calculate Squares and Cubes ********************\n')
    print(' Please enter your choice of execution:\n  1. Sequential\n  2. Parallel (Multithreading)\n')
    choice = input('  Choice: ')
    numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print(f'\n Input numbers: {numbers}')

    start = time.perf_counter()

    if choice == '1':
        go_sequential(numbers)
    elif choice == '2':
        go_parallel(numbers)
    else:
        print('\nError: Wrong Choice. Correct values - [1, 2].\n')
        return

    end = time.perf_counter()
    elapse_time = round(end - start, 2)

    print(f'\n Square List: {square_list}')
    print(f' Cube List: {cube_list}')
    print(f'\n Elapsed Time: {elapse_time}\n')

# Sequential processing.


def go_sequential(numbers):
    print('\nSequential Processing')
    calculate_square(numbers)
    calculate_cube(numbers)

# Parallel Processing.


def go_parallel(numbers):
    print('\nParallel Processing')
    square = threading.Thread(target=calculate_square, args=(numbers, ))
    cube = threading.Thread(target=calculate_cube, args=(numbers, ))

    square.start()
    cube.start()

    square.join()
    cube.join()


if __name__ == '__main__':
    main()
