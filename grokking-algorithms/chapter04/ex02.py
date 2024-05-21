# Write a recursive function to count the number of items in a list.

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([]))
print(count([3]))
print(count([1, 2, 3]))
