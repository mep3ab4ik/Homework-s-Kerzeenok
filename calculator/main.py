"""Давай калькулятор делать со звездочкой

Калькулятор хранит значение последнего выражения. По умолчанию — 0.

Пользователь вводит строку. В строке пользователь может ввести число и оператор —
это +-/* (плюс, минут, делить, умножить). Число и оператор всегда разделяются пробелами.
 Для очистки последнего сохранённого результата пользователь может ввести C.
Примеры входных строк:
+ 1
1 + 1
10 * 2
/ 2
C

Если введено 2 числа и между ними оператор — нужно выполнить соответствующую операцию.
Если введены оператор и одно число, то нужно выполнить соответствующую операцию,
где левое число — это результат последнего выражения.
Причём обязательна важна данная последовательность, что сначала оператор, а потом число.

Для неверного формата ввода выкидывать ошибку WrongInput.
Для неверного оператора ошибку UnknownOperator.

Реализовать это в классе. Каждый оператор калькулятора —
отдельный метод. Итого должно быть 5 методов класса калькулятора, включая конструктор."""

from error import WrongInput, UnknownOperator
from calculator import Calculator
from decimal import Decimal


def computation(number_1, operator, number_2):
    """Функция для обработки знаков вычисление"""

    star = Calculator()

    if operator == "=":
        star.plus(number_1, number_2)
    elif operator == "-":
        star.minus(number_1, number_2)
    elif operator == "*":
        star.multiply(number_1, number_2)
    elif operator == "/":
        star.divide(number_1, number_2)
    else:
        raise UnknownOperator("Неизвестный оператор, попробуйте снова!")


def check_data(data):
    start = Calculator()

    # Проверка на очистку памяти

    if data[0] in ["ce", "c"]:
        print("Очистили память")
        start.last_memory = 0

    # TODO можно проще
    if len(data) == 2:
        number_1 = start.last_memory
        number_2 = data[-1]
        operator = data[-2]
    elif len(data) == 3:
        number_1 = data[0]
        number_2 = data[-1]
        operator = data[-2]

    # TODO Конвертируем в формат Decimal
    number_1 = Decimal(number_1)
    number_2 = Decimal(number_2)

    computation(number_1, operator, number_2)


def main():
    while True:
        data = input("Введите выражение: ").lower()

        data = data.strip().split(" ")

        try:
            check_data(data)
        except UnknownOperator as e:
            print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()
