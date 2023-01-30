# Алгоритмы

# Сортировка СЛИЯНИЕМ

def list_merging(list1, list2):
    result_list = []
    size1 = len(list1)
    size2 = len(list2)

    i = 0
    j = 0

    while i < size1 and j < size2:
        if list1[i] <= list2[j]:
            result_list.append(list1[i])
            i += 1
        else:
            result_list.append(list2[j])
            j += 1

    # if size1 > size2:
    #     while i < size1:
    #         result_list.append(list1[i])
    #         i += 1
    # else:
    #     while j < size2:
    #         result_list.append(list2[j])
    # тоже самое только короче

    result_list += list1[i:] + list2[j:]
    return result_list


def list_sorting(list):
    half = len(list) // 2
    result_list1 = list[:half]
    result_list2 = list[half:]

    if len(result_list1) > 1:
        result_list1 = list_sorting(result_list1)

    if len(result_list2) > 1:
        result_list2 = list_sorting(result_list2)

    return list_merging(result_list1, result_list2)


my_list = [6, 3, 7, 1, 4, 2, 9, 8, 5]
print(list_sorting(my_list))

# Сделать алгоритм сортировки
