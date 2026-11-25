
# Assessment 3.7: Sorting Algorithms
# Name: LEYMAR PALAGTIOSA

# Unsorted Array (Duplicate letters removed)
unsorted_array = [
    "L", "E", "Y", "M", "A", "R",
    "P", "G", "T", "I", "O", "S"
]

# Copy the unsorted array
sorted_array = unsorted_array.copy()


# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Sort the array
bubble_sort(sorted_array)


# Display Results
print("SORTING ALGORITHM")
print("Name: LEYMAR PALAGTIOSA")

print("\nUNSORTED ARRAY:")
print(unsorted_array)

print("\nSORTED ARRAY:")
print(sorted_array)
