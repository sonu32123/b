def lru_page_replacement(reference_string, frame_size):
    # Initialize variables
    page_faults = 0
    frames = []
    recent_usage = {}

    for time, page in enumerate(reference_string):
        if page not in frames:
            # Page fault occurs
            page_faults += 1
            if len(frames) < frame_size:
                # Add the page if frames are not full
                frames.append(page)
            else:
                # Replace the least recently used page
                # Find the LRU page (one with the smallest timestamp)
                lru_page = min(frames, key=lambda p: recent_usage[p])
                frames.remove(lru_page)
                frames.append(page)

            print(f"Page: {page} -> Frames: {frames} (Page Fault)")
        else:
            print(f"Page: {page} -> Frames: {frames}")

        # Update recent usage for the current page
        recent_usage[page] = time

    return page_faults


# Input reference string and frame size
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 3

# Display input
print(f"Reference String: {reference_string}")
print(f"Frame Size: {frame_size}\n")

# Compute the number of page faults
page_faults = lru_page_replacement(reference_string, frame_size)

# Display the result
print(f"\nTotal Page Faults: {page_faults}")
