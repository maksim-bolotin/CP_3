from utils import get_operations_data, reading_from_file


def main():
    data = reading_from_file()
    get_operations_data(data)


if __name__ == '__main__':
    main()
