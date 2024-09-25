from lib import count_common_elements
import unittest

class TestCountCommonElements(unittest.TestCase):
    # Блок 1: Тесты для случая, когда переданы непустые списки
    def test_common_elements_present(self):
        # Общие элементы есть
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        list3 = [4, 5, 6, 7]
        list4 = [4, 8, 9]
        self.assertEqual(count_common_elements(list1, list2, list3, list4), 1)  # Только 4 общий

        # Несколько общих элементов
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        list3 = [3, 5, 6]
        self.assertEqual(count_common_elements(list1, list2, list3), 1)  # Общий только 3

    # Блок 2: Тесты для случая, когда общих элементов нет
    def test_no_common_elements(self):
        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        self.assertEqual(count_common_elements(list1, list2, list3), 0)  # Нет общих элементов

    # Блок 3: Тесты для случая с пустыми и одноэлементными списками
    def test_empty_lists(self):
        self.assertEqual(count_common_elements(), 0)  # Пустой аргумент, должен вернуть 0
        self.assertEqual(count_common_elements([]), 0)  # Один пустой список
        self.assertEqual(count_common_elements([], []), 0)  # Несколько пустых списков
        self.assertEqual(count_common_elements([1]), 1)  # Один элемент в одном списке
        self.assertEqual(count_common_elements([1], []), 0)  # Один элемент и пустой список

    # Блок 4: Тесты для случая, когда переданы одинаковые списки
    def test_identical_lists(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = [1, 2, 3]
        self.assertEqual(count_common_elements(list1, list2, list3), 3)  # Все элементы общие

    # Блок 5: Тесты для случая, когда списки содержат дубликаты
    def test_lists_with_duplicates(self):
        list1 = [1, 1, 2, 2, 3, 3]
        list2 = [1, 2, 3, 3, 4]
        list3 = [2, 2, 3, 3, 5]
        self.assertEqual(count_common_elements(list1, list2, list3), 2)  # Общие только 2 и 3 (без учета дубликатов)

if __name__ == '__main__':
    unittest.main()
