__author__ = "Керзеёнок Никита"

from random import randint
from datetime import datetime
from authenticator import Authenticator


# def guess_number_game() -> None:
#     """Это функция по угадыванию числа
#
#     Просим пользователя ввести число от 0 до 5
#     затем функции записывает случайное число от 0 до 5 в переменную.
#     Сравниваем значение и в зависимости от условия выдает нужно f-строку.
#     Если мы угадали число возвращает f-строку c победой.
#     """
#
#     # Счетчик количества попыток
#     game_count = 0
#
#     number_random = randint(0, 5)
#
#     while True:
#         you_number = input("Please play game. Enter a number from 0 to 5: ")
#
#         # Удаляем пробелы и перезаписываем в одноименную переменную
#         you_number = you_number.strip()
#
#         # Обработка исключение на недопустимое значение
#
#         try:
#             you_number = int(you_number)
#         except ValueError:
#             print("You have entered symbols, you need to enter numbers")
#             game_count += 1
#             continue
#
#         if you_number > number_random:
#             print("Enter a number less than.")
#         elif you_number < number_random:
#             print("Enter a number greater than.")
#         else:
#             print(f"You WIN! It's {number_random}!. Try number: {game_count + 1}")
#             break
#
#         game_count += 1


def main() -> None:
    login = input("Введите логин: ")
    password = input("Введите пароль:")
    account = Authenticator()

    if account.login:


    # guess_number_game()


if __name__ == '__main__':
    main()
