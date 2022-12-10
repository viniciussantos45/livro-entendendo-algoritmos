def counter(arr_list):
    if len(arr_list) == 0:
        return 0

    return 1 + counter(arr_list[1:])


print(counter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(counter([1, 2, 3, 4]))
