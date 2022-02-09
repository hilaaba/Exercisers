def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""
    # Напечатать имя функции
    print(f'Тестируем функцию: {sorting_algorithm.__name__}')

    source = [1, 3, 2, 4]
    expected_answer = [1, 2, 3, 4]
    assert sorting_algorithm(source) == expected_answer, (
        f'Алгоритм {sorting_algorithm.__name__} работает неправильно со списком с натуральными числами'
    )

    source = [0, -1000, 2, 4]
    expected_answer = [-1000, 0, 2, 4]
    assert sorting_algorithm(source) == expected_answer, (
        f'Алгоритм {sorting_algorithm.__name__} работает неправильно со списком с отрицательными числами и с нулем'
    )

    source = [1, 1, 1, 1]
    expected_answer = [1, 1, 1, 1]
    assert sorting_algorithm(source) == expected_answer, (
        f'Алгоритм {sorting_algorithm.__name__} работает неправильно со списком с одинаковыми числами'
    )

    source = []
    expected_answer = []
    assert sorting_algorithm(source) == expected_answer, (
        f'Алгоритм {sorting_algorithm.__name__} работает неправильно с пустой строкой'
    )

    print(f'Тест для {sorting_algorithm.__name__} пройден')


# Ипортируем тестируемые функции из пакета ttd_sprint5_data
test_sort(ttd_sprint5_data.bubble_sort)
test_sort(ttd_sprint5_data.timsort_sort)
test_sort(ttd_sprint5_data.selection_sort)
test_sort(ttd_sprint5_data.insertion_sort)
test_sort(ttd_sprint5_data.cap_sort)
test_sort(ttd_sprint5_data.merge_sort)
test_sort(ttd_sprint5_data.heap_sort)
test_sort(ttd_sprint5_data.stepa_sort)
test_sort(ttd_sprint5_data.quick_sort)
test_sort(ttd_sprint5_data.sus_sort)