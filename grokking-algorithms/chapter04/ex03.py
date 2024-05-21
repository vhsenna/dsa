# Write a recursive function to find the maximum number in a list.

def max(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        max_num = max(list[1:])
        if list[0] > max_num:
            return list[0]
        else:
            return max_num


print(max([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 99, 5]))
