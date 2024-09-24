def count_common_elements(*lists):
    if not lists:
        return 0

    # Используем множество для хранения элементов первого списка
    common_elements = set(lists[0])

    # Перебираем остальные списки и находим пересечения
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)


# Пример использования функции:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
list4 = [4, 8, 9]

count = count_common_elements(list1, list2, list3, list4)
print(f'Количество одинаковых элементов: {count}')
