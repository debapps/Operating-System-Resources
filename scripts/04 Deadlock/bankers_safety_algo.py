import numpy as np
import pandas as pd
import os


# This program implements the Banker's Algorithm using Python modules - Pandas and NumPy.

# Global Verialbles - Input Directory and files.
inputDir = r'./Resource_Allocation_State_data'
AllocationFile = os.path.join(inputDir, 'Allocation.json')
MaxFile = os.path.join(inputDir, 'Max.json')
AvailableFile = os.path.join(inputDir, 'Available.json')
RequestFile = os.path.join(inputDir, 'Request.json')


def main():
    print('\n************** Deadlock Avoidance Algorithms ****************\n')

    # Getting all the Matrices from the JSON files.
    Allocation = pd.read_json(AllocationFile, orient='index').to_numpy()
    Max = pd.read_json(MaxFile, orient='index').to_numpy()
    Available = pd.read_json(AvailableFile, orient='index').to_numpy()[0]
    Request = pd.read_json(RequestFile, orient='index').to_numpy()[0]
    process_count = Allocation.shape[0]
    resource_count = Allocation.shape[1]

    # Calculation of Need Matrix.
    Need = Max - Allocation

    # Preparation of Resource Allocation State.
    resource_allocation_state = [
        Allocation.copy(),
        Max.copy(),
        Need.copy(),
        Available.copy(),
        process_count,
        resource_count
    ]

    # Display the Matrices
    print(
        f'\nProcess Count - {process_count} | Resource Count - {resource_count}\n')
    print(f'Allocation Matrix:\n {Allocation}\n')
    print(f'Max Matrix:\n {Max}\n')
    print(f'Need Matrix:\n {Need}\n')
    print(f'Available Matrix:\n {Available}\n')

    # Fetch the choice of Algoritms.

    # Display Menu.
    print('\n Choose the algorithms to execute ...')
    print('\n1. Safety Algorithm.\n2. Banker\'s Algorithm.')
    choice = input('Enter your choice [1, 2]: ')

    if choice == '1':
        # Execute the safety algorithm with current resource allocation state.
        safety_algo(resource_allocation_state)
    elif choice == '2':
        print('\n************** Banker\'s Algorithm ****************\n')

        # Get the request process.
        req_process = input('Which process requests resources? ')
        req_process_id = int(req_process[-1])
        print(f'Request Matrix of {req_process}:\n {Request}\n')

        # Calling the Banker's Algorithm with new request for resources.
        response = bankers_algo(
            resource_allocation_state, req_process_id, Request)
        print(response)

        print('\n************ End Banker\'s Algorithm **************\n')
    else:
        print('ERROR!! Wrong choice.')

    print('\n************** End Deadlock Avoidance Algorithms ****************\n')


def bankers_algo(resource_allocation_state, req_process_id, Request):
    # Get all the Matrices of Resource Allocation State.
    Allocation, Max, Need, Available, process_count, resource_count = resource_allocation_state

    # Check if the request is invalid.
    # If the Request Matrix > the Need Matrix, then the request is invalid.
    if np.any(Request > Need[req_process_id, :]):
        msg = f'\nThe Request of process P{req_process_id} is invalid!'
        return msg

    # Check if the process requires to wait.
    # If the Request Matrix > Available Matrix, then the process requires to wait for resources.
    if any(Request > Available):
        msg = f'\nThe Process P{req_process_id} requires to wait for resources.'
        return msg

    # Change the resource allocation state to create new resource allocation state.
    Available = Available - Request
    Allocation[req_process_id, :] = Allocation[req_process_id, :] + Request
    Need[req_process_id, :] = Need[req_process_id, :] - Request

    new_allocation_state = [
        Allocation.copy(),
        Max.copy(),
        Need.copy(),
        Available.copy(),
        process_count,
        resource_count
    ]

    # Call the Safety Algorithm with new resource allocation state.
    safe_state = safety_algo(new_allocation_state)

    if safe_state:
        msg = f'\nThe Process P{req_process_id} is allocated resources as per request - {Request}.'
        return msg
    else:
        # Previous Resource Allocation State is restored.
        Available = Available + Request
        Allocation[req_process_id, :] = Allocation[req_process_id, :] - Request
        Need[req_process_id, :] = Need[req_process_id, :] + Request
        msg = f'\nThe Process P{req_process_id} is NOT allocated resources as per request - {Request}.'
        return msg


def safety_algo(resource_allocation_state):
    print('\n************** Safety Algorithm ****************\n')
    # Get all the Matrices of Resource Allocation State.
    Allocation, Max, Need, Available, process_count, resource_count = resource_allocation_state

    print(f'Allocation Matrix:\n {Allocation}\n')
    print(f'Max Matrix:\n {Max}\n')
    print(f'Need Matrix:\n {Need}\n')
    print(f'Available Matrix:\n {Available}\n')

    # Create the list of finish flags.
    Finish = [False for i in range(process_count)]

    # Create the safe sequnce of the processes.
    safe_sequence = []
    Track = []

    while True:
        for i in range(process_count):
            if Finish[i] == False and np.all(Need[i, :] <= Available):
                Available += Allocation[i, :]
                Finish[i] = True
                safe_sequence.append(f'P{i}')

                print('\nResource State')
                print(f'Available: {Available}')
                print(f'Finish State: {Finish}')
                print(f'safe_sequence: {safe_sequence}')

                continue
            else:
                Track = Finish.copy()

        if Track == Finish:
            break

    safe_state = None

    if all(Finish):
        print(f'\nThe System is safe. Safe Sequence - {safe_sequence}')
        safe_state = True
    else:
        print('\nThe System is NOT safe.')
        safe_state = False

    print('\n************ End Safety Algorithm **************\n')
    return safe_state


if __name__ == '__main__':
    main()
