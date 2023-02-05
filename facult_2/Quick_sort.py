def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        elem = array[0]
        # генерируем список с использованием функции фильтра
        # и всё что меньше elem добавляем влево
        left = list(filter(lambda x: x < elem, array))
        # генератор списка который равен elem (обход по всем элементам
        # списка s и добавление i если оно равно elem)
        center = [i for i in array if i == elem]
        # генерируем список с использованием функции фильтра и всё
        # что больше elem добавляем вправо
        right = list(filter(lambda x: x > elem, array))

        # Вызываем рекурсивно левую и правую часть отсортированных списков
        return quick_sort(left) + center + quick_sort(right)


print(quick_sort([7, 6, 10, 5, 7, 9, 8, 7, 3, 4]))
