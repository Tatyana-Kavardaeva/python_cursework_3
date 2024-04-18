from utils import get_executed_operations, sort_operations_by_date, display_operations


if __name__ == "__main__":
    count_operation = 5
    executed_operations = get_executed_operations("../operations.json")
    sorted_operations = sort_operations_by_date(executed_operations)
    display_operations(sorted_operations, count_operation)
