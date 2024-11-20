#include <iostream>
#include <vector>

using namespace std;

// Function to check if the system is in a safe state
bool isSafeState(vector<vector<int>>& allocation, vector<vector<int>>& max, vector<int>& available) {
    int processes = allocation.size();
    int resources = allocation[0].size();

    // Calculate the Need matrix
    vector<vector<int>> need(processes, vector<int>(resources));
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    // Initialize work and finish arrays
    vector<int> work = available;
    vector<bool> finish(processes, false);
    vector<int> safeSequence;

    // Find processes that can finish
    for (int count = 0; count < processes; count++) {
        bool found = false;
        for (int i = 0; i < processes; i++) {
            if (!finish[i]) {
                bool canFinish = true;
                for (int j = 0; j < resources; j++) {
                    if (need[i][j] > work[j]) {
                        canFinish = false;
                        break;
                    }
                }
                if (canFinish) {
                    for (int j = 0; j < resources; j++) {
                        work[j] += allocation[i][j];
                    }
                    safeSequence.push_back(i);
                    finish[i] = true;
                    found = true;
                }
            }
        }
        if (!found) {
            // If no process can finish, return false
            cout << "System is not in a safe state.\n";
            return false;
        }
    }

    // If all processes can finish, print the safe sequence
    cout << "System is in a safe state.\nSafe Sequence: ";
    for (int i : safeSequence) {
        cout << "P" << i << " ";
    }
    cout << endl;
    return true;
}

int main() {
    int processes, resources;

    // Input the number of processes and resources
    cout << "Enter the number of processes: ";
    cin >> processes;
    cout << "Enter the number of resources: ";
    cin >> resources;

    // Input Allocation, Maximum, and Available matrices
    vector<vector<int>> allocation(processes, vector<int>(resources));
    vector<vector<int>> max(processes, vector<int>(resources));
    vector<int> available(resources);

    cout << "Enter the Allocation matrix:\n";
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            cin >> allocation[i][j];
        }
    }

    cout << "Enter the Maximum matrix:\n";
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            cin >> max[i][j];
        }
    }

    cout << "Enter the Available resources vector:\n";
    for (int i = 0; i < resources; i++) {
        cin >> available[i];
    }

    // Check if the system is in a safe state
    isSafeState(allocation, max, available);

    return 0;
}
