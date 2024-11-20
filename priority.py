import heapq

def calculate_priority(processes, burst_time, arrival_time, priority, preemptive=True):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = burst_time[:]
    time = 0
    completed = 0
    min_heap = []

    if preemptive:
        # Preemptive Priority Scheduling
        while completed < n:
            # Add all arrived processes to the heap
            for i in range(n):
                if arrival_time[i] <= time and remaining_time[i] > 0:
                    heapq.heappush(min_heap, (priority[i], i))

            if min_heap:
                # Get the process with the highest priority (lowest value)
                _, i = heapq.heappop(min_heap)
                time += 1
                remaining_time[i] -= 1
                if remaining_time[i] == 0:
                    completed += 1
                    completion_time[i] = time
            else:
                time += 1
    else:
        # Non-Preemptive Priority Scheduling
        ready_queue = []
        while completed < n:
            # Add all arrived processes to the ready queue
            for i in range(n):
                if arrival_time[i] <= time and remaining_time[i] > 0:
                    heapq.heappush(ready_queue, (priority[i], i))

            if ready_queue:
                # Get the process with the highest priority (lowest value)
                _, i = heapq.heappop(ready_queue)
                time += burst_time[i]
                completion_time[i] = time
                remaining_time[i] = 0
                completed += 1
            else:
                time += 1

    # Calculate Turnaround Time (TAT) and Waiting Time (WT)
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    # Display the results
    mode = "Preemptive" if preemptive else "Non-Preemptive"
    print(f"{mode} Priority Scheduling Results:")
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}{'Completion Time':<20}{'TAT':<10}{'WT':<10}")
    for i in range(n):
        print(f"{processes[i]:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{priority[i]:<10}{completion_time[i]:<20}{turnaround_time[i]:<10}{waiting_time[i]:<10}")
    
    # Calculate and display averages
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


# Example Input
processes = ["P1", "P2", "P3", "P4"]
burst_time = [8, 4, 9, 5]
arrival_time = [0, 1, 2, 3]
priority = [2, 1, 4, 3]  # Lower value = Higher priority

# Run Priority Scheduling
print("===" * 10)
calculate_priority(processes, burst_time, arrival_time, priority, preemptive=True)
print("===" * 10)
calculate_priority(processes, burst_time, arrival_time, priority, preemptive=False)
