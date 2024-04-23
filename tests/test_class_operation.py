from src.class_operation import Operation


def get_operation_data():
    return {
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


def get_operation():
    operations = get_operation_data()
    return Operation(operations['date'], operations['description'], operations.get('from'), operations['to'],
                          operations['operationAmount'])


def test_mask_card_number():
    operation = get_operation()
    assert operation.mask_card_number() == "Maestro 1596 83** **** 5199"


def test_mask_account_number():
    operation = get_operation()
    assert operation.mask_account_number() == "Счет **9589"


def test_formatted_amount():
    operation = get_operation()
    assert operation.formatted_amount() == "31957.58 руб."


def test_formatted_date():
    operation = get_operation()
    assert operation.formatted_date() == "26.08.2019"


def test___str__():
    operation = get_operation()
    assert operation.__str__() == ("26.08.2019 Перевод организации\n"
        "Maestro 1596 83** **** 5199 -> Счет **9589\n"
        "31957.58 руб.\n")
