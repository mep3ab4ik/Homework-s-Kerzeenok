# Kerzeenok

import os.path
import json
from datetime import datetime
from exceptions import AuthorizationError, RegistrationError


class Authenticator:
    """Класс аутентификации пользователя."""

    def __init__(self):

        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0
        self.user = {
            "login": f"{self.login}",
            "password": f"{self._password}",
            "time": f"{self.last_success_login_at}",
            "errors_count": f"{self.errors_count}"}

        # Проверка на наличия файла 'auth.txt'

        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """Метод, который проверяет на наличия файла.

        Если файл существует, то возвращает True иначе Else.
        """

        return os.path.exists('auth.json')

    def _read_auth_file(self):
        """Метод считывания данных.

        Метод считывает данные из файла и перезаписываем их в переменные.
        """

        # Записываем данные в переменные

        with open("auth.json", "r") as f:

            # Считываем данные из файла в dict

            self.user = json.load(f)

            # Записываем в локальные переменные

            self.login = self.user["login"]
            self._password = self.user["password"]

            # Конвертируем полученное значение к datetime и записываем

            self.last_success_login_at = datetime.fromisoformat(self.user.get("time"))
            self.errors_count = int(self.user["errors_count"])



    def authorize(self, login, password):
        """Метод авторизации пользователя

        Проверяет на наличие переменной 'login'.
        Сравнивает введенные логин и пароль, с логином и паролем из файла.
        """

        if not self.login:
            self.errors_count += 1
            raise AuthorizationError("You haven't registered.")

        if not login:
            self.errors_count += 1
            raise AuthorizationError("The login field cannot be empty.")

        if login == self.login and password == self._password:
            self._update_auth_file()
            self.last_success_login_at = datetime.utcnow()
        else:
            self.errors_count += 1
            raise AuthorizationError("The username or password is incorrect")

    def _update_auth_file(self):
        """Метод обновление данных в файле.

        В файле обновляется время и количество ошибок.
        """

        # Записываем в файл с помочью json

        with open("auth.json", "w") as f:
            # Записываем время по ключу в форме строки
            json.dump(self.user, f)

    def registrate(self, login, password):
        """Метод регистрации пользователя.

        Если файл существует, то выводит ошибку.
        Если нет, то создаем файл и записываем туда данные.

        """
        if self.user["login"] is None:
            self.errors_count += 1
            raise RegistrationError("You are already a registered user.")

        if not login:
            self.errors_count += 1
            raise RegistrationError("The login field cannot be empty.")

        self.user.update({"login": f"{login}",
                          "password": f"{password}",
                          "time": f"{datetime.utcnow()}"})
        self._update_auth_file()


class Validator:
    """Класс валидации почты и пароля"""

    def __init__(self):
        pass

    def validate_password(self):
        pass