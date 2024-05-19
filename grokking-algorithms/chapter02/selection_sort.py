# Finds the smallest value in an array
def find_smallest(array):
    # Stores the smallest value
    smallest = array[0]

    # Stores the index of the smallest value
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest_index = i
            smallest = array[i]
    return smallest_index


# Sort array
def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


print(selection_sort([5, 3, 6, 2, 10]))
