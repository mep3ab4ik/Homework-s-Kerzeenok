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

def main():

    """"""
    # Переменная со всеми операторами

    operators = {"+", "-", "*", "/"}

    # Первое число и последней вывод

    start = Calculator()

    while True:
        data = input("Введите выражение: ").lower()

        # Стоп программы

        if data == "stop":
            exit()

        # Проверка на очистку памяти

        if data == "c" or data == "ce":
            print("Очистили память")
            start.last_memory = 0
            continue

        data = data.strip().split(" ")

        # TODO ПЕРЕПИСАТЬ СУКА НАДО БЛЯТЬ
        if len(data) == 2:
            number_1 = start.last_memory
            number_2 = data[-1]
            operator = data[-2]
        elif len(data) == 3:
            number_1 = data[0]
            number_2 = data[-1]
            operator = data[-2]

        # try:
        #     if number_1

        try:
            if operator not in operators:
                raise UnknownOperator("Неизвестный оператор, попробуйте снова!")
        except UnknownOperator as e:
            print(f"Ошибка: {e}\n")
            continue

        # TODO Конвертируем в формат Decimal
        number_1 = Decimal(number_1)
        number_2 = Decimal(number_2)

        if operator == "+":
            start.plus(number_1, number_2)

        if operator == "-":
            start.minus(number_1, number_2)

        if operator == "*":
            start.multiply(number_1, number_2)

        try:
            if operator == "/":
                start.divide(number_1, number_2)
        except WrongInput as e:
            print(f"Ошибка: {e}\n")
            continue

        print("Получилось значение:", start.last_memory)


if __name__ == '__main__':
    main()
