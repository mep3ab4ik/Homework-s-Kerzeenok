# Kerzeenok

import re
from authenticator import RegistrationError


class Validator:
    """Класс валидации почты и пароля"""

    errors_count: int = 0

    def __init__(self, email: str, password: str):

        self.email = email
        self.password = password

        self.validate_email(self.email)
        self.validate_password(self.password)


    @classmethod
    def validate_password(cls, password: str):
        """Класс валидацию для пароля.

        Пароль должен содержать:
        -минимум 4 символа,
        -минимум один заглавный символ,
        -минимум один строчная символ,
        -минимум одна цифра,
        -минимум один спецсимвол."""

        if not password:
            cls.errors_count += 1
            raise RegistrationError("The password field cannot be empty.")

        # Паттерн для пароля

        pattern_password = r"(?=.*[A-ZА-ЯЁ])(?=.*[a-zа-яё])(?=.*[0-9])(?=.*[!@#$%^&*])[0-9A-zА-яёЁ!@#$%^&*]{4,}"

        # Возвращает список всех найденных совпадений. Если их нет, возвращает пустой список

        result = re.findall(pattern_password, password)

        # Проверка на пустой список

        if not result:
            cls.errors_count += 1
            raise RegistrationError("Password not valid.The password must contain at least 4 symbols, "
                                    "at least 1 uppercase letter, at least 1 lowercase letter, "
                                    "at least 1 digit and at least 1 special symbol.")


    @classmethod
    def validate_email(cls, email: str):
        """Класс для валидации email.

        Email должен иметь следующий порядок:
        -любые символы,
        -знак '@',
        -любые буквы или цифры,
        -знак '.',
        -буквы.
        """

        if not email:
            cls.errors_count += 1
            raise RegistrationError("The email field cannot be empty.")

        # Паттерн для email

        pattern_email = r"(?=[A-z]).*@\w+\.[A-z]*"

        # Возвращает список всех найденных совпадений. Если их нет, возвращает пустой список

        result = re.findall(pattern_email, email)

        # Проверка на пустой список

        if not result:
            cls.errors_count += 1
            raise RegistrationError("Email not valid.")
