from json import load
from classes.operation import Operation


def reading_from_file() -> list[dict]:
    """
    Получение списка операций из файла.
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return load(file)


def get_operations_data(operations: list[dict]) -> list[Operation]:
    """
    Распаковка данных, полученных из файла.
    """
    operations_data = []
    for operation in operations:
        if operation and operation["state"] == "EXECUTED":
            operation_data = Operation(
                id_=operation["id"],
                date=operation["date"],
                state=operation["state"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to_=operation["to"]
            )
            operations_data.append(operation_data)
    return operations_data


def sort_date(operations: list[Operation]) -> list[Operation]:
    """
    Сортировка списка операций по дате совершения.
    """
    return sorted(operations, key=lambda operation: operation.date)
