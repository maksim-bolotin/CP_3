from utils import get_operations_data, reading_from_file, sort_date


def main():
    # загрузка данных об операциях.
    data = reading_from_file()
    # создание объектов класса из каждой операции.
    list_of_data = get_operations_data(data)
    # сортировка объектов класса по дате выполнения операции.
    last_dates = sort_date(list_of_data)
    # реализация вывода последних пяти выполненных (EXECUTED) операций.
    for i in last_dates[-5:]:
        print(i)


if __name__ == '__main__':
    main()
