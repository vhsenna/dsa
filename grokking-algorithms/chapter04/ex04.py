# Remember binary search from chapter 1? It's a D&C algorithm, too. Can you come up with the base case and recursive
# case for binary search?

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []

        for i in array[1:]:
            if i <= pivot:
                less.append(i)
        for i in array[1:]:
            if i > pivot:
                greater.append(i)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
