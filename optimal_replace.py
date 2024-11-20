def optimal_page_replacement(reference_string, frame_size):
    # Initialize variables
    page_faults = 0
    frames = []

    # Function to find the farthest page in future
    def find_farthest_page(frames, reference_string, current_index):
        farthest = -1
        page_to_replace = -1
        for page in frames:
            try:
                # Find the index of the next occurrence of the page in the reference string
                next_use = reference_string.index(page, current_index)
            except ValueError:
                # If the page is not found in the future, it is the best candidate for replacement
                return page
            if next_use > farthest:
                farthest = next_use
                page_to_replace = page
        return page_to_replace

    for i, page in enumerate(reference_string):
        # If the page is not in the frames, it's a page fault
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                # Add the page to the frame if there is space
                frames.append(page)
            else:
                # Find the page to replace using the optimal algorithm
                page_to_replace = find_farthest_page(frames, reference_string, i)
                frames.remove(page_to_replace)
                frames.append(page)

            print(f"Page: {page} -> Frames: {frames} (Page Fault)")
        else:
            print(f"Page: {page} -> Frames: {frames}")

    return page_faults


# Input reference string and frame size
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 3

# Display input
print(f"Reference String: {reference_string}")
print(f"Frame Size: {frame_size}\n")

# Compute the number of page faults
page_faults = optimal_page_replacement(reference_string, frame_size)

# Display the result
print(f"\nTotal Page Faults: {page_faults}")
