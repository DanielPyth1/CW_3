from settings import OPERATIONS_JSON_PATH, LAST_NUMBER_OPERATION
from src.utils import load_json, filter_executed_operations, sort_operations_by_date, covert_payment_date, \
    mask_credit_card_and_account


def main():
    operations = load_json(OPERATIONS_JSON_PATH)
    executed_operations = filter_executed_operations(operations)
    sorted_operations = sort_operations_by_date(executed_operations)

    index_operation = 0
    for operation in sorted_operations:

        index_operation += 1
        if index_operation > LAST_NUMBER_OPERATION:
            break

        print(covert_payment_date(operation.get('date', '')), ' ',
              operation.get('description', ''), '\n',
              mask_credit_card_and_account(operation.get('from', '')),
              '-> ',
              mask_credit_card_and_account(operation.get('to', '')), '\n',
              f"{operation.get('operationAmount', '').get('amount', '')} ",
              f"{operation.get('operationAmount', '').get('currency', '').get('name', '')}\n",
              sep=''
              )


if __name__ == '__main__':
    main()

