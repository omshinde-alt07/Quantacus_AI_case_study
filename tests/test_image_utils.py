import pytest

from utils.image_utils import (
    clean_price,
    calculate_discount,
)


def test_clean_price():

    assert clean_price("₹1,299") == 1299


def test_discount():

    assert calculate_discount(
        500,
        350,
    ) == 30


def test_no_discount():

    assert calculate_discount(
        500,
        500,
    ) == 0


def test_invalid_discount():

    with pytest.raises(ValueError):

        calculate_discount(
            100,
            150,
        )