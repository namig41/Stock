import datetime
from datetime import date
from pytest import fixture

from domain.entities.batch import Batch
from domain.value_objects.order_line import OrderLine


@fixture
def today():
    return date.today()


@fixture
def tomorrow():
    return date.today() + datetime.timedelta(days=1)


@fixture
def later():
    return datetime.date.today() + datetime.timedelta(days=100)
