import json
from src.class_operation import Operation


def get_all_operations(file):
    """Читает json файл и преобразует в объект"""
    with open(file, "r", encoding='utf-8') as f:
        all_operations = json.load(f)
        return all_operations


def get_executed_operations(all_operations):
    """Возвращает список словарей выполненныx операций"""
    executed_operations = []
    for dict_operation in all_operations:
        if dict_operation.get('state') == 'EXECUTED':
            executed_operations.append(dict_operation)
    return executed_operations


def sort_operations_by_date(list_operations):
    """Принимает список операций и сортирует их по дате в порядке убывания"""
    sorted_operations = sorted(list_operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations


def get_operations(sorted_operations):
    """Формирует список экземпляров Операций из словарей с данными операций"""
    list_operations = []
    for operations in sorted_operations:
        operation = Operation(operations['date'], operations['description'], operations.get('from'), operations['to'],
                              operations['operationAmount'])
        list_operations.append(operation)
    return list_operations


def display_operations(list_operations, count_operation):
    """Выводит указанное количество операций из списка экземпляров операций по шаблону:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 USD"""
    result = ''
    list_operations = list_operations[:count_operation]
    for operation in list_operations:
        result += f"{operation}\n"
    return result
