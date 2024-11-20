def round_robin(processes, burst_time, arrival_time, time_quantum):
    n = len(processes)
    remaining_time = burst_time[:]
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    queue = []
    visited = [False] * n
    completed = 0

    while completed < n:
        # Add processes to the queue based on arrival time
        for i in range(n):
            if arrival_time[i] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True
        
        if queue:
            # Get the first process from the queue
            current = queue.pop(0)
            
            # Execute the process
            if remaining_time[current] > time_quantum:
                time += time_quantum
                remaining_time[current] -= time_quantum
            else:
                time += remaining_time[current]
                completion_time[current] = time
                remaining_time[current] = 0
                completed += 1
            
            # Add the process back to the queue if not completed
            if remaining_time[current] > 0:
                queue.append(current)
            
            # Add newly arrived processes to the queue
            for i in range(n):
                if arrival_time[i] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        else:
            time += 1  # If no process is ready, increment time

    # Calculate TAT and WT
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    # Display the results
    print(f"Round Robin Scheduling (Time Quantum = {time_quantum}) Results:")
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Completion Time':<20}{'TAT':<10}{'WT':<10}")
    for i in range(n):
        print(f"{processes[i]:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{completion_time[i]:<20}{turnaround_time[i]:<10}{waiting_time[i]:<10}")

    # Calculate and display averages
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
burst_time = [5, 8, 7, 3]
arrival_time = [0, 1, 2, 3]
time_quantum = 3

# Run Round Robin Scheduling
print("===" * 10)
round_robin(processes, burst_time, arrival_time, time_quantum)
