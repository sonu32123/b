def calculate_fcfs(processes, burst_time, arrival_time):
    n = len(processes)
    
    # Initialize lists for calculations
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    # Calculate Completion Time (CT)
    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            if arrival_time[i] > completion_time[i - 1]:
                completion_time[i] = arrival_time[i] + burst_time[i]
            else:
                completion_time[i] = completion_time[i - 1] + burst_time[i]
    
    # Calculate Turnaround Time (TAT) and Waiting Time (WT)
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    # Display the results
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Completion Time':<20}{'TAT':<10}{'WT':<10}")
    for i in range(n):
        print(f"{processes[i]:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{completion_time[i]:<20}{turnaround_time[i]:<10}{waiting_time[i]:<10}")
    
    # Calculate and display average TAT and WT
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]

# Run the FCFS Scheduling Algorithm
calculate_fcfs(processes, burst_time, arrival_time)
