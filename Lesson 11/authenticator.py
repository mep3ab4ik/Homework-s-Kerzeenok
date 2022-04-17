# Kerzeenok

import os.path
import json
import hashlib
import ast
from datetime import datetime
from exceptions import AuthorizationError, RegistrationError
from validate import Validator


class Authenticator:
    """Класс аутентификации пользователя."""

    def __init__(self):
        self.email: str | None = None
        self._password: dict | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0
        self.salt: bytes = b""
        self.key: bytes = b""
        self.user = {
            "email": f"{self.email}",
            "password": self._password,
            "time": f"{self.last_success_login_at}",
            "errors_count": f"{self.errors_count}"
        }

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

            self.user = json.loads(f.read())

            # Из dict раскидываем по переменным

            self.email = self.user["email"]
            self._password = self.user["password"]

            # Конвертируем полученное значение к datetime и записываем

            self.last_success_login_at = datetime.fromisoformat(self.user.get("time"))
            self.errors_count = int(self.user["errors_count"])

        """Функция 'ast.literal_eval' определяет, является ли данные для вычисления,
        допустимым типом после вычисления. Если это так, то выполняет операцию.
        В нашем случае байты допустимое значение"""

        # Вычисляем данные и записываем значение ключа salt в переменную self.salt

        self.salt = ast.literal_eval(self._password.get("salt"))

        # Вычисляем данные и записываем значение ключа key в переменную self.key

        self.key = ast.literal_eval(self._password.get("key"))


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

        # Создаем новый хэш для проверки

        new_key = hashlib.pbkdf2_hmac(
            "sha512",  # Используемый алгоритм хеширования
            password.encode("utf-8"),  # Конвертируем пароль в байты
            self.salt,  # Предоставляем соль
            100000  # Количество итераций (минимум 100.000)
        )

        if email == self.email and new_key == self.key:
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
            f.write(json.dumps(self.user, indent=0))

    def registrate(self, data: Validator):
        """Метод регистрации пользователя.

        Если файл существует, то выводит ошибку.
        Если нет, то создаем файл и записываем туда данные.
        """

        if self.email:
            self.errors_count += 1
            raise RegistrationError("You are already a registered user.")


        email = data.email
        password = data.password
        self.errors_count += data.errors_count

        # Генерируем соль

        self.salt = os.urandom(32)

        """Используем библиотеку hashlib для хэширование пароля.
        Хорошая функция хэширования паролей должна быть настраиваемой, медленной и содержать соль.
        hmac это псевдослучайная функция. Атрибут hash_name - это желаемый алгоритм хэширования для hmac.
        В нашем случаем мы используем SHA512. Так как при переборе хэша, скорость составит ~220 M/s,
        для SHA256 составит ~2050 M/s. (M- мегахэши)."""

        # Создаем хэш пароля

        key = hashlib.pbkdf2_hmac(
            "sha512",  # Используемый алгоритм хеширования
            password.encode("utf-8"),  # конвертируем пароль в байты
            self.salt,  # Предоставляем соль
            100000)  # Количество итераций (минимум 100.000 итераций)

        # Создаем dict, где храним значение salt и key в одноименных ключах

        hash_password = {"salt": f"{self.salt}", "key": f"{key}"}

        # Обновляем dict user

        self.user.update({"email": email,
                          "password": hash_password,
                          "time": datetime.utcnow().isoformat(),
                          "errors_count": self.errors_count})

        self._update_auth_file()
