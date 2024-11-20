import threading

# Function to compute a single element in the result matrix
def compute_element(result, A, B, row, col):
    # Compute the dot product of A's row and B's column
    result[row][col] = sum(A[row][k] * B[k][col] for k in range(len(B)))
    print(f"Thread computing element [{row}][{col}] completed.")

def matrix_multiply(A, B):
    # Get the dimensions of matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Ensure matrix dimensions are compatible for multiplication
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions are incompatible for multiplication.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # List to hold threads
    threads = []

    # Create threads for each element of the result matrix
    for i in range(rows_A):
        for j in range(cols_B):
            thread = threading.Thread(target=compute_element, args=(result, A, B, i, j))
            threads.append(thread)
            thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return result


# Example matrices for multiplication
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# Perform matrix multiplication
result = matrix_multiply(A, B)

print("\nResultant Matrix:")
for row in result:
    print(row)
