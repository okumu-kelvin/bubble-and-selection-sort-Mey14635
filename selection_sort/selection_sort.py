def selection_sort(arr):
    # Go through each index i in the list except the last
    for i in range(len(arr) - 1):
        minpos = i  # Track the position of the smallest value
        for j in range(i, len(arr)):  # Compare with the rest of the array
            if arr[j] < arr[minpos]:
                minpos = j
        # Swap the elements
        temp = arr[i]
        arr[i] = arr[minpos]
        arr[minpos] = temp

    return arr  # Return the sorted list

# Test the function
arr = [5, 4, 3, 2, 1, 0]
selection_sort(arr)
print(arr)
