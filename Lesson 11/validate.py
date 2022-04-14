# Kerzeenok

import re
from authenticator import RegistrationError


class Validator:
    """Класс валидации почты и пароля"""

    def __init__(self):

        # Паттерн для пароля

        self.pattern_password = r"(?=.*[A-ZА-ЯЁ])(?=.*[a-zа-яё])(?=.*[0-9])(?=.*[!@#$%^&*])[0-9A-zА-яёЁ!@#$%^&*]{4,}"

        # Паттерн для email

        self.pattern_email = r"(?=[A-z])\w+@\w+\.[A-z]*"


    def validate_password(self, password: str):
        """Класс валидацию для пароля, который содержит(Ищет по паттерну):
        минимум 4 символа,
        минимум один заглавный символ,
        минимум один прописной символ,
        минимум одна цифра,
        минимум один спецсимвол."""

        result = re.findall(self.pattern_password, password)

        if not result:
            raise RegistrationError("Password not valid.")

    def validate_email(self, email: str):
        """Класс для валидации email(Ищет по паттерну):
        вначале есть цифры или букву,
        присутствует @,
        есть цифры или буквы,
        стоит точка,
        есть буквы.
        """

        result = re.findall(self.pattern_email, email)

        if not result:
            raise RegistrationError("Email not valid.")