import pytest
from datetime import datetime
from classes.operation import Operation


@pytest.fixture()
def get_data_list():
    return [
        {
            "id": 260972664,
            "state": "EXECUTED",
            "date": "2018-01-23T01:48:30.477053",
            "operationAmount": {
                "amount": "2974.30",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 3414396880443483",
            "to": "Visa Gold 2684274847577419"
        },
        {
            "id": 317987878,
            "state": "EXECUTED",
            "date": "2018-01-13T13:00:58.458625",
            "operationAmount": {
                "amount": "55985.82",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 8906171742833215",
            "to": "Visa Platinum 6086997013848217"
        },
        {
            "id": 72122709,
            "state": "EXECUTED",
            "date": "2018-12-18T17:07:09.800800",
            "operationAmount": {
                "amount": "19683.25",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 86675623828180311969",
            "to": "Счет 15351391408911677994"
        },
        {
            "id": 242885401,
            "state": "EXECUTED",
            "date": "2019-07-08T00:08:32.986663",
            "operationAmount": {
                "amount": "10083.68",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38427597486442637521",
            "to": "Счет 83889757415570699323"
        }
    ]


@pytest.fixture()
def get_operation_data(get_data_list):
    operation_data = []
    for operation in get_data_list:
        if operation and operation["state"] == "EXECUTED":
            operation_data.append(Operation(
                id_=operation["id"],
                date=operation["date"],
                state=operation["state"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to_=operation["to"]
            )
            )
    return operation_data


def test_convert_data(get_operation_data):
    operation = get_operation_data[0]
    assert operation.convert_data("Visa Classic 3414396880443483") == "Visa Classic 3414 39** **** 3483"
    assert operation.convert_data("Счет 86675623828180311969") == "Счёт ****1969"
    assert operation.convert_data(" ") is None
    assert operation.convert_data("") is None
    assert operation.convert_data("XXXXXX XXXXXXXXXX") is None
    assert operation.convert_data("Maestro 8906171742833215") == "Maestro 8906 17** **** 3215"
    assert operation.convert_data("MasterCard 8906171742833215") == "MasterCard 8906 17** **** 3215"


def test_date_converter(get_operation_data):
    operation = get_operation_data[0]
    assert operation.date_converter("2018-01-23T01:48:30.477053") == datetime(2018, 1, 23, 1, 48, 30, 477053)


def test___str__(get_operation_data):
    operation = get_operation_data[0]
    assert operation.__str__() == """23.01.2018 Перевод с карты на карту
Visa Classic 3414 39** **** 3483 -> Visa Gold 2684 27** **** 7419
2974.30 USD\n"""


def test__init__(get_operation_data):
    operation = get_operation_data[0]
    assert operation.id_ == 260972664
    assert operation.date == datetime(2018, 1, 23, 1, 48, 30, 477053)
    assert operation.state == "EXECUTED"
