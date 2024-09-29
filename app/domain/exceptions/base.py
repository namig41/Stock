from application.exceptions.base import ApplicationException


class DomainException(ApplicationException):
    @property
    def message(self):
        return "Ошибка предметной области"
