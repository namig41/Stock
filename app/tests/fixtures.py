from infrastructure.container.init import _init_container
from punq import Container


def init_dummy_container() -> Container:
    container: Container = _init_container()
    return container
