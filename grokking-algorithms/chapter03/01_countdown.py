def countdown(i):
    # Base case
    print(i)
    if i <= 1:
        return
    # Recursive case
    else:
        countdown(i - 1)


countdown(3)
