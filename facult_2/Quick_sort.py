def quick_sort(s):
    if len(s) <= 1:
        return s
    else:
        elem = s[0]
        # генерируем список с использованием функции фильтра и всё что меньше elem добавляем влево
        left = list(filter(lambda x: x < elem, s))
        # генератор списка который равен elem (обход по всем элементам списка s и добавление i если оно равно elem)
        center = [i for i in s if i == elem]
        # генерируем список с использованием функции фильтра и всё что больше elem добавляем вправо
        right = list(filter(lambda x: x > elem, s))

        # Вызываем рекурсивно левую и правую часть отсортированных списков
        return quick_sort(left) + center + quick_sort(right)


print(quick_sort([7, 6, 10, 5, 7, 9, 8, 7, 3, 4]))
