import datetime
from datetime import date

from infrastructure.container.init import init_container
from punq import Container
from pytest import fixture


@fixture
def container() -> Container:
    return init_container()


@fixture
def today() -> date:
    return date.today()


@fixture
def tomorrow() -> date:
    return date.today() + datetime.timedelta(days=1)


@fixture
def later() -> date:
    return datetime.date.today() + datetime.timedelta(days=100)
