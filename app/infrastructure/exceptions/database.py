from dataclasses import dataclass

from infrastructure.exceptions.base import InfrastuctureException


@dataclass
class ConnectionErrorTODataBaseException(InfrastuctureException):
    @property
    def message(self):
        return "Ошибка подключения к базе данных"
