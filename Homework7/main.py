__author__ = "Керзеёнок Никита"

from random import randint
from authenticator import Authenticator
from exceptions import AuthorizationError, RegistrationError


def guess_number_game() -> None:
    """Это функция по угадыванию числа

    Просим пользователя ввести число от 0 до 5
    затем функции записывает случайное число от 0 до 5 в переменную.
    Сравниваем значение и в зависимости от условия выдает нужно f-строку.
    Если мы угадали число возвращает f-строку c победой.
    """

    # Счетчик количества попыток
    game_count = 0

    number_random = randint(0, 5)

    while True:
        you_number = input("Please play game. Enter a number from 0 to 5: ")

        # Удаляем пробелы и перезаписываем в одноименную переменную
        you_number = you_number.strip()

        # Обработка исключение на недопустимое значение

        try:
            you_number = int(you_number)
        except ValueError:
            print("You have entered symbols, you need to enter numbers")
            game_count += 1
            continue

        if you_number > number_random:
            print("Enter a number less than.")
        elif you_number < number_random:
            print("Enter a number greater than.")
        else:
            print(f"You WIN! It's {number_random}!. Try number: {game_count + 1}")
            break

        game_count += 1


def main() -> None:
    """Это основанная функция для работы.

    Выводим подсказу пользователю, что ему нужно сделать в бесконечном цикле запрашиваем логин и пароль.
    Если существует аккаунт, то пытаемся авторизоваться и когда авторизуемся играем в игру, затем прерываем цикл
    Если не существует аккаунт, то регистрируем его и заканчиваем цикл.
    """

    account = Authenticator()

    # Проверка на подсказку регистрации\авторизации

    if account.login:
        print("To log in, enter your username and password. \n")
    else:
        print("To register in, enter your username and password.\n")

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if account.login:

            try:
                account.authorize(username, password)
            except AuthorizationError as e:
                print(f"Error. {e}")
                continue

            success_login_time = account.last_success_login_at.strftime('%d.%m.%Y %H:%M:%S')

            print(f"Hello {account.login}! "
                  f"Time of the last successful authorization: {success_login_time}. "
                  f"Quantity of authorization attempts: {account.errors_count}")

            guess_number_game()
            break

        if not account.login:

            try:
                account.registrate(username, password)
            except RegistrationError as e:
                print(f"Error. {e}")
                continue

            print("You have successfully registered")
            break


if __name__ == '__main__':
    main()
