def fifo_page_replacement(reference_string, frame_size):
    # Initialize variables
    page_faults = 0
    frames = []
    
    # Process each page in the reference string
    for page in reference_string:
        if page not in frames:
            # Page fault occurs if the page is not in the current frames
            page_faults += 1
            if len(frames) < frame_size:
                # Add the page to the frames if space is available
                frames.append(page)
            else:
                # Replace the oldest page (FIFO) if the frame is full
                frames.pop(0)
                frames.append(page)
        # Print the state of frames after each step
        print(f"Page: {page} -> Frames: {frames} {'(Page Fault)' if page not in frames else ''}")
    
    return page_faults


# Input reference string and frame size
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 3

# Display input
print(f"Reference String: {reference_string}")
print(f"Frame Size: {frame_size}\n")

# Compute the number of page faults
page_faults = fifo_page_replacement(reference_string, frame_size)

# Display the result
print(f"\nTotal Page Faults: {page_faults}")
