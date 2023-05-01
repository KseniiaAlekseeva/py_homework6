# Return the indices of elements which are in range [a,b]
def indices_in_range(sl: list, a: int, b: int) -> list:
    result = [(i, sl[i]) for i in range(len(sl)) if sl[i] >= a and sl[i] <= b]
    return result


some_list = [1, -4, 5, 3, 7, 9, 12]
a = -4
b = 5

print(indices_in_range(some_list, a, b))
