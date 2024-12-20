from dataclasses import dataclass

from infrastructure.exceptions.base import InfrastuctureException


@dataclass
class BatchNotFoundInDataException(InfrastuctureException):
    @property
    def message(self):
        return "Продукт не найден в базе данных"
