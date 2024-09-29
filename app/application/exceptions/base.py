class ApplicationException(Exception):
    @property
    def message(self):
        return "Ошибка приложения"
