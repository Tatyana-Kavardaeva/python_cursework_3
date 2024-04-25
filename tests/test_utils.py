import os
from src.class_operation import Operation
from src.utils import get_all_operations, get_executed_operations, sort_operations_by_date, display_operations, get_operations


current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "..", "data")
file_path = os.path.join(data_dir, "test_operations.json")


def test_get_all_operations():
    assert len(get_all_operations(file_path)) == 3


def test_get_executed_operations():
    all_operations = get_all_operations(file_path)
    assert len(get_executed_operations(all_operations)) == 2


def test_sort_operations_by_date():
    operations = [
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2019-07-03T18:35:29.512364"}
    ]
    sorted_operations = sort_operations_by_date(operations)
    assert sorted_operations == [
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"}
    ]


def test_display_operations():
    list_operations = [
        Operation(date='2019-08-26T10:50:58.294041', description='Перевод организации',
                  where_from='Maestro 1596837868705199', to='Счет 64686473678894779589',
                  operationamount={'amount': '31957.58',
                                   'currency': {'name': 'руб.', 'code': 'RUB'}}),
        Operation(date='2019-07-03T18:35:29.512364', description='Перевод организации',
                  where_from='MasterCard 7158300734726758', to='Счет 35383033474447895560',
                  operationamount={'amount': '8221.37',
                                   'currency': {'name': 'USD', 'code': 'USD'}})
    ]
    count_operation = 2
    result = display_operations(list_operations, count_operation)
    expected_output = (
        "26.08.2019 Перевод организации\n"
        "Maestro 1596 83** **** 5199 -> Счет **9589\n"
        "31957.58 руб.\n\n"
        "03.07.2019 Перевод организации\n"
        "MasterCard 7158 30** **** 6758 -> Счет **5560\n"
        "8221.37 USD\n\n"
    )

    assert result == expected_output
