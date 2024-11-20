def is_safe_state(processes, available, max_need, allocated):
    num_processes = len(processes)
    num_resources = len(available)

    # Calculate the need matrix
    need = [[max_need[i][j] - allocated[i][j] for j in range(num_resources)] for i in range(num_processes)]

    print("Need Matrix:")
    for row in need:
        print(row)

    # Initialize work and finish arrays
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found_process = False
        for i in range(num_processes):
            if not finish[i]:
                # Check if the process's needs can be satisfied with available resources
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    # Satisfy the process
                    print(f"Process {processes[i]} can be executed.")
                    for j in range(num_resources):
                        work[j] += allocated[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found_process = True
                    break
        if not found_process:
            # If no process can proceed, the system is not in a safe state
            print("No process can proceed further. System is NOT in a safe state.")
            return False, []
    
    print("All processes executed successfully. System is in a safe state.")
    return True, safe_sequence


# Example data
processes = ["P0", "P1", "P2", "P3", "P4"]
available = [3, 3, 2]
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Display input data
print("Available Resources:", available)
print("Max Need Matrix:")
for row in max_need:
    print(row)
print("Allocated Resources:")
for row in allocated:
    print(row)

# Check if the system is in a safe state
is_safe, safe_sequence = is_safe_state(processes, available, max_need, allocated)

if is_safe:
    print("\nSafe Sequence:", " -> ".join(safe_sequence))
else:
    print("\nThe system is in an unsafe state.")
