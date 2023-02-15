from module import result
import pytest


def test_result_1():
    expected_true = "Сбалансированно"
    test_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '[([])((([[[]]])))]{()}']
    for i in test_list:
        res = result(i)
        assert expected_true == res


def test_result_2():
    expected_false = "Несбалансированно"
    test_list = ['}{}', '{{[(])]}}', '[[{())}]']
    for i in test_list:
        res = result(i)
        assert expected_false == res
