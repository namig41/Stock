import datetime
from datetime import date

from pytest import fixture


@fixture
def today():
    return date.today()


@fixture
def tomorrow():
    return date.today() + datetime.timedelta(days=1)


@fixture
def later():
    return datetime.date.today() + datetime.timedelta(days=100)
