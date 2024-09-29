from domain.exceptions.base import DomainException


class OutOfStock(DomainException):
    sku: str

    @property
    def message(self):
        return f"Артикула {self.sku} нет в наличии"
