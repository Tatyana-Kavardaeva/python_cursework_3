import os
from utils import get_all_operations, get_executed_operations, sort_operations_by_date, display_operations, get_operations


if __name__ == "__main__":
    count_operation = 5
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, "operations.json")
    all_operations = get_all_operations(file_path)
    executed_operations = get_executed_operations(all_operations)
    sorted_operations = sort_operations_by_date(executed_operations)
    operations = get_operations(sorted_operations)
    print(display_operations(operations, count_operation))

