import json
from src.utils import get_executed_operations, sort_operations_by_date, display_operations
from src.class_operation import Operation


def test_get_executed_operations():
  assert len(get_executed_operations("test_operations.json")) == 2


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
  sorted_operations = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]
  count_operation = 2

  result = display_operations(sorted_operations, count_operation)

  # Проверяем вывод функции с использованием capfd
  #   captured = capfd.readouterr()
  expected_output = (
  "26.08.2019 Перевод организации\n"
  "Maestro 1596 83** **** 5199 -> Счет **9589\n"
  "31957.58 руб.\n"
  "03.07.2019 Перевод организации\n"
  "MasterCard 7158 30** **** 6758 -> Счет **5560\n"
  "8221.37 USD\n"
  )

  assert result == expected_output


def test_mask_card_number():
  operations =  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
  where_from = operations.get('from')
  operation = Operation(operations['date'], operations['description'], where_from, operations['to'],
                        operations['operationAmount'])
  assert operation.mask_card_number() == "Maestro 1596 83** **** 5199"