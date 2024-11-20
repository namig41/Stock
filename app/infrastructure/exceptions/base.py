from dataclasses import dataclass

from application.exceptions.base import ApplicationException


@dataclass
class InfrastuctureException(ApplicationException):
    @property
    def message(self):
        return "Ошибка на уровне ифраструктры"
