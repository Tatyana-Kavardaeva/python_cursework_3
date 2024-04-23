import json
from src.class_operation import Operation


def get_executed_operations(file):
    """Получает данные по операциям из json файла и возвращает список словарей выполненныx операций"""
    with open(file, "r", encoding="utf-8") as f:
        operations = json.load(f)
        executed_operations = []
        for operation in operations:
            if operation.get('state') == 'EXECUTED':
                executed_operations.append(operation)
        return executed_operations


def sort_operations_by_date(list_operations):
    """Принимает список операций и сортирует их по дате в порядке убывания"""
    sorted_operations = sorted(list_operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations


def display_operations(sorted_operations, count_operation):
    """Выводит указанное количество операций из отсортированного списка по шаблону:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 USD"""
    result = ''
    list_operations = sorted_operations[:count_operation]
    for operations in list_operations:
        operation = Operation(operations['date'], operations['description'], operations.get('from'), operations['to'],
                              operations['operationAmount'])
        result += f"{operation}\n"
    return result
