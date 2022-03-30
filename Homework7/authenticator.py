import os.path
from datetime import datetime
from exceptions import AuthorizationError, RegistrationError


class Authenticator:

    def __init__(self):

        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        # Проверка на наличия файла 'auth.txt'

        if self._is_auth_file_exist():
            self._read_auth_file()


    def _is_auth_file_exist(self) -> bool:
        """Метод, который проверяет на наличия файла.

        Если файл существует, то возвращает True иначе Else.
        """

        return os.path.exists('auth.txt')


    def _read_auth_file(self):
        """Метод считывания данных.

        Метод считывает данные из файла и записывает их в переменные.
        """
        with open('auth.txt') as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = f.readline().strip()
            self.errors_count = int(f.readline().strip())


    def authorize(self, login, password):
        """Метод авторизации пользователя

        Проверяет на наличие переменной 'login'.
        Сравнивает введенные логин и пароль, с логином и паролем из файла.
        """

        if not self.login:
            raise AuthorizationError("Вы не зарегистрировались.")

        if login:
            if login == self.login and password == self._password:
                self.last_success_login_at = datetime.utcnow().isoformat()
                self._update_auth_file()
            else:
                self.errors_count += 1
                self._update_auth_file()
                raise AuthorizationError("Логин или пароль неверные")
        else:
            raise AuthorizationError("Логин не может быть пустым")


    def _update_auth_file(self):
        """Метод обновление данных в файле.

        В файле обновляется время и количество ошибок.
        """

        with open('auth.txt', 'w') as f:
            f.write(f"{self.login}\n")
            f.write(f"{self._password}\n")
            f.write(f"{self.last_success_login_at}\n")
            f.write(f"{self.errors_count}")


    def registrate(self, login, password):
        """Метод регистрации пользователя.

        Если файл существует, то выводит ошибку.
        Если нет, то создаем файл и записываем туда данные.

        """
        if self.login:
            raise RegistrationError("Вы уже зарегистрированный пользователь.")

        if login:
            with open('auth.txt', 'w+') as f:
                f.write(f"{login}\n")
                f.write(f"{password}\n")
                f.write(f"{datetime.utcnow().isoformat()}\n")
                f.write(f"{self.errors_count}\n")
        else:
            raise RegistrationError("Поля логин не может быть пустым.")
