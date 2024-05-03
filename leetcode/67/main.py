def addBinary(a: str, b: str) -> str:
    a_int = int(a, 2)
    b_int = int(b, 2)

    sum_int = a_int + b_int

    return str(bin(sum_int)[2:])


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
