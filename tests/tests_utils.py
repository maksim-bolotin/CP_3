import pytest
from datetime import datetime
from utils import reading_from_file, sort_date, get_operations_data


def test_reading_from_file():
    test_data = reading_from_file()
    assert type(test_data) is list
    assert len(test_data) == 101


def test_get_operations_data():
    data = reading_from_file()
    operations = get_operations_data(data)
    assert operations[0].id_ == 441945886
    assert operations[0].date == datetime(2019, 8, 26, 10, 50, 58, 294041)
    assert operations[0].state == "EXECUTED"


def test_sort_date():
    test_list = []
    data = reading_from_file()
    operations = get_operations_data(data)
    updatetd_operations_list = sort_date(operations)
    for data in updatetd_operations_list:
        test_list.append(data)
    assert test_list[-1].date == datetime(2019, 12, 8, 22, 46, 21, 935582)
