import numpy as np
import pandas as pd
import os

# This program implements the deadlock detection algorithm.

# Global Verialbles - Input Directory and files.
inputDir = r'./Deadlock_Detection_Resource_State'
AllocationFile = os.path.join(inputDir, 'Allocation.json')
AvailableFile = os.path.join(inputDir, 'Available.json')
RequestFile = os.path.join(inputDir, 'Request.json')


def main():
    print('\n************** Deadlock Detection Algorithm ****************\n')

    # Getting all the Matrices from the JSON files.
    Allocation = pd.read_json(AllocationFile, orient='index').to_numpy()
    Available = pd.read_json(AvailableFile, orient='index').to_numpy()[0]
    Request = pd.read_json(RequestFile, orient='index').to_numpy()
    process_count = Allocation.shape[0]
    resource_count = Allocation.shape[1]

    # Preparation of Resource Allocation State.
    resource_allocation_state = [
        Allocation.copy(),
        Available.copy(),
        Request.copy(),
        process_count,
        resource_count
    ]

    # Invoking the deadlock detection algorithm.
    deadlock_detection_algo(resource_allocation_state)

    print('\n************** Deadlock Detection Algorithm ****************\n')


def deadlock_detection_algo(resource_allocation_state):

    # Get all the Matrices of Resource Allocation State.
    Allocation, Available, Request, process_count, resource_count = resource_allocation_state

    print(
        f'Process Count - {process_count} | Resource Count - {resource_count}\n')
    print(f'Allocation Matrix:\n {Allocation}\n')
    print(f'Available Matrix:\n {Available}\n')
    print(f'Request Matrix:\n {Request}\n')

    # Create the list of finish flags.
    Finish = [False for i in range(process_count)]

    for i in range(process_count):
        if np.all(Allocation[i, :] == [0, 0, 0]):
            Finish[i] = True

    # Create the safe sequnce of the processes.
    deadlock_processes = []
    Track = []

    while True:
        for i in range(process_count):
            if Finish[i] == False and np.all(Request[i, :] <= Available):
                Available += Allocation[i, :]
                Finish[i] = True

                print('\nResource State')
                print(f'Process - P{i}')
                print(f'Request[{i}]: {Request[i, :]}')
                print(f'Available: {Available}')
                print(f'Finish State: {Finish}')

                continue
            else:
                Track = Finish.copy()

        if Track == Finish:
            break

    if all(Finish):
        print('\nThe System is NOT in Deadlock.')
    else:
        for i in range(process_count):
            if Finish[i] == False:
                deadlock_processes.append(f'P{i}')
        print(
            f'\nThe following processes are in Deadlock! {deadlock_processes}')


if __name__ == '__main__':
    main()
