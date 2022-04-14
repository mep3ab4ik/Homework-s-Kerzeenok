# Kerzeenok

import os.path
import json
from datetime import datetime
from exceptions import AuthorizationError, RegistrationError


class Authenticator:
    """Класс аутентификации пользователя."""


    def __init__(self):

        self.email: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0
        self.user = {
            "email": f"{self.email}",
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

            self.email = self.user["email"]
            self._password = self.user["password"]

            # Конвертируем полученное значение к datetime и записываем

            self.last_success_login_at = datetime.fromisoformat(self.user.get("time"))
            self.errors_count = int(self.user["errors_count"])



    def authorize(self, email, password):
        """Метод авторизации пользователя

        Проверяет на наличие переменной 'email'.
        Сравнивает введенные логин и пароль, с логином и паролем из файла.
        """

        if not self.email:
            self.errors_count += 1
            raise AuthorizationError("You haven't registered.")

        if not email:
            self.errors_count += 1
            raise AuthorizationError("The email field cannot be empty.")

        if email == self.email and password == self._password:
            self._update_auth_file()
            self.last_success_login_at = datetime.utcnow()
        else:
            self.errors_count += 1
            raise AuthorizationError("The email or password is incorrect")

    def _update_auth_file(self):
        """Метод обновление данных в файле.

        В файле обновляется время и количество ошибок.
        """

        # Записываем в файл с помочью json

        with open("auth.json", "w") as f:
            # self.user["errors_count"] = str(self.errors_count)
            # Записываем время по ключу в форме строки
            json.dump(self.user, f)

    def registrate(self, email, password):
        """Метод регистрации пользователя.

        Если файл существует, то выводит ошибку.
        Если нет, то создаем файл и записываем туда данные.
        """

        if self.email:
            self.errors_count += 1
            raise RegistrationError("You are already a registered user.")

        if not email:
            self.errors_count += 1
            raise RegistrationError("The email field cannot be empty.")

        if not password:
            self.errors_count += 1
            raise RegistrationError("The password filed cannot be empty.")

        self.user.update({"email": f"{email}",
                          "password": f"{password}",
                          "time": f"{datetime.utcnow()}",
                          "errors_count": f"{self.errors_count}"})
        self._update_auth_file()
        