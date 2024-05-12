import json
from datetime import datetime
from pathlib import Path

def load_json(path):
    """
    Выгружаю файл .json
    """
    with open(path, "r", encoding='UTF-8') as file:
        return json.load(file)


def filter_executed_operations(operations):
    """
    Фильтрация операций по статусу EXECUTED
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]

def sort_operations_by_date(operations):
    """
    Сортирует операции по дате в убывающем порядке
    """
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)


def covert_payment_date(date):
    """
    Выводим ДД.ММ.ГГГГ
    """
    iso_date = datetime.fromisoformat(date)
    return iso_date.strftime("%d.%m.%Y")


def mask_credit_card_and_account(payment_info):
    """
    Маскирование номера карты и счета
    """
    if payment_info.startswith('Счет'):
        return f'Счет **{payment_info[-4:]} '
    elif payment_info != '':
        return (
            f'{payment_info[:-12]}'
            f' {payment_info[-11:-9]}'
            f'** **** {payment_info[-4:]} '
        )
    return ''







