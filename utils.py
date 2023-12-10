from json import load


def reading_from_file() -> dict:
    """
    Получение списка операций из файла
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return load(file)
