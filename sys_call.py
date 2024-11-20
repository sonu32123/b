import os
import time
import subprocess

def demonstrate_system_calls():
    print("Demonstrating System Calls (Windows-Compatible):")
    
    # 1. getpid() - Get the current process ID
    print(f"Current Process ID (getpid): {os.getpid()}")
    
    # 2. spawn - Create a new process (using subprocess)
    print("Spawning a new process...")
    process = subprocess.Popen(["python", "-c", "print('Hello from the new process!')"])
    print(f"Spawned Process ID: {process.pid}")
    
    # 3. wait() - Wait for the spawned process to complete
    print("Waiting for the spawned process to complete...")
    process.wait()
    print(f"Process completed with return code: {process.returncode}")
    
    # 4. execute a command (similar to exec())
    print("Executing a command to list files in the current directory...")
    result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    print("Command Output:\n", result.stdout)
    
    # 5. sleep() - Simulate a delay in the process
    print("Simulating a delay using sleep()...")
    time.sleep(2)
    print("Delay complete. Exiting program.")
    
if __name__ == "__main__":
    demonstrate_system_calls()
