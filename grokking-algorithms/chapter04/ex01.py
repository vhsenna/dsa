# Write out the code for the earlier sum function.

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([]))
print(sum([3]))
print(sum([1, 2, 3]))
