def sum(arr_list):
    if len(arr_list) == 0:
        return 0
    return arr_list[0] + sum(arr_list[1:])


print(sum([1, 2, 10]))
