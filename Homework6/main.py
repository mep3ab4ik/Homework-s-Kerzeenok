from validator import Validator
from validator import DataWithDate
from exceptions import ValidationError

from random import randint
from datetime import datetime


def get_passport_advice(age: int) -> str | None:
    """Это функция проверки возраста на совет

    В случае, если возраст находится в одном из диапазонов,
    выдает совет по этому условию.
    """

    if 16 <= age <= 17:
        return " Please get first passport."

    if 25 <= age <= 26:
        return " Please replace first passport."

    if 45 <= age <= 46:
        return " Please replace second passport."


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

    Функция запрашивает имя и возраст, затем вызывает другие функции для прохождения валидации.
    Если валидация прошла успешна, записывает данные в переменную и останавливает цикл.
    Если валидация не прошла, выводит ошибку и цикл начинается сначала.
    Цикл будет выполниться до тех пор, пока валидация не пройдет успешна.
    """

    # Счетчик попыток ввода данных
    error_count = 0

    # Определение объекта validate_data класса Validator
    validate_data = Validator()
    time_start = datetime.utcnow()

    while True:
        if error_count > 0:
            print(f"You are trying to enter data {error_count+1} times.\n")

        name = input("Enter your name: ")
        age = input("Enter your age: ")

        # Определение объекта data c передачей name и age класса DataWithDate
        data = DataWithDate(name, age)

        # Обработка исключение на некорректное имя или возраст

        try:
            validate_data.validate(data)
        except ValidationError as e:
            print(f"Error. Data entered incorrectly. Check out the text error: {e}\n")
            error_count += 1
        else:
            break

    advice = get_passport_advice(data.age)
    text_welcome = f"Hello {name .title()}! You age is {age}."

    if advice:
        text_welcome += advice

    print(f"\nYou trying enter a data: {error_count + 1} times. Time of the first attempt -{time_start}."
          f" Time of the last attempt - {data.time_end}\n")
    print(text_welcome)
    guess_number_game()



if __name__ == '__main__':
    main()