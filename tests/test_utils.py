from src.utils import covert_payment_date, mask_credit_card_and_account, sort_operations_by_date, \
    filter_executed_operations

def test_filter_executed_operations():
    assert filter_executed_operations([{'state': 'EXECUTED'}, {}, {'state': 'BWIND'}]) == [{'state': 'EXECUTED'}]


def test_sort_operations_by_date():
    assert sort_operations_by_date([{'date': 6}, {'date': 8}]) == [{'date': 8}, {'date': 6}]


def test_covert_payment_date():
    assert covert_payment_date('2019-07-03T18:35:29.512364') == '03.07.2019'


def test_mask_credit_card_and_account():
    assert mask_credit_card_and_account('Счет 11776614605963066702') == 'Счет **6702 '
    assert mask_credit_card_and_account('Visa Classic 7022985698476865') == 'Visa Classic 7022 85** **** 6865 '
    assert mask_credit_card_and_account('') == ''