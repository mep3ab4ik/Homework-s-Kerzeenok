# Kerzeenok

from exceptions import ValidationError
from datetime import datetime


class Data:
    """Класс хранящий данные о пользователе"""

    def __init__(self, name: str, age: str):
        """Волшебный Метод, который записывает имя и возраст в переменные с помощью конструктора класса
        и очищает от пробелов, пересохранив в одноименные перченные.
        """

        self.name = name
        self.age = age

        self._clear_whitespaces()

        self.age = int(self.age)


    def _clear_whitespaces(self):
        """Метод, который удаляет пробелы в начале и конце строки"""

        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """Класс-наследник от Базового класса (Data).

    Сохранять текущее время, когда был создан этот экземпляр класса.
    """


    def __init__(self, name: str, age: str):
        """Волшебный метод, в котором наследуется имя и возраст от родительского класса.
        Также храниться переменная временим создания, когда обращались к классу.
        """

        super().__init__(name, age)
        self.time_end = datetime.utcnow()


class Validator:
    """Класс валидации данных"""


    def __init__(self):
        """Волшебный метод, в котором создаем пустой список в экземпляре класса."""
        self.data_history: list[Data] = []


    def validate(self, data: Data):
        """Метод, который передает имя и возраст из класса Data

        Записываем данные в переменные и добавляем их в список
        """

        self.data_history.append(data)

        self._validate_name()
        self._validate_age()


    def _validate_name(self):
        """Это метод проверки имени на определенные условия

        Проверка имени на пустоту, содержит ли имя больше одного пробела
        и минимальное количество символов в имени - 3.
        """

        # Один из вариантов
        if not self.data_history:
            raise ValueError("the object is not passed, do not touch class")

        if not self.data_history[-1].name:
            raise ValidationError("You not enter your name.")
        elif self.data_history[-1].name.count(" ") > 1:
            raise ValidationError("Your name contains more than 1 space. ")
        elif len(self.data_history[-1].name) < 3:
            raise ValidationError("Your name is short, the minimum number of letters in the name is 3. ")


    def _validate_age(self,):
        """Это метод проверки возраста

        Проверяет, что возраст не ноль или отрицательный,
        проверяет, что минимальный возраст - 14.
        """

        # Один из вариантов
        if not self.data_history:
            raise ValueError("the object is not passed, do not touch class")

        if self.data_history[-1].age < 1:
            raise ValidationError("You age is 0 or negative.")
        elif self.data_history[-1].age < 14:
            raise ValidationError("Minimum age is 14.")
