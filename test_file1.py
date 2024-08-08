import pytest
from lab1_1 import is_positive_triple_number, digits_sum, number_ratio, number_difference


@pytest.mark.parametrize("number,sum_of_digits", [(124, 7), (792, 18),
                                                  (100, 1)])
def test_digits_sum(number, sum_of_digits):
    assert digits_sum(number) == sum_of_digits


@pytest.mark.parametrize("number,difference", [(124, 297), (792, 495),
                                               (100, 99)])
def test_difference(number, difference):
    assert number_difference(number) == difference


@pytest.mark.parametrize("number,ratio", [(124, 17.714), (792, 44),
                                          (100, 100)])
def test_ratio(number, ratio):
    assert number_ratio(number) == ratio


def test_is_positive_number():
    assert is_positive_triple_number(-20) == False
    assert is_positive_triple_number(-124) == False
    assert is_positive_triple_number(534) == True
    assert is_positive_triple_number(375) == True

def test_is_triple_number():
    assert is_positive_triple_number(55) == False
    assert is_positive_triple_number(47) == False
    assert is_positive_triple_number(529) == True
    assert is_positive_triple_number(891) == True
