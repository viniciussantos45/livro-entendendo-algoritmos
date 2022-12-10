def max(arr_list):
    if len(arr_list) == 0:
        return 0

    max_value = max(arr_list[1:])

    return max_value if max_value > arr_list[0] else arr_list[0]


print(max([1, 2, 32, 4, 5, 6, 7, 8, 9]))
print(max([1, 2, 3, 4]))
print(max([1]))
