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
from decimal import Decimal, InvalidOperation

start = Calculator()


def computation(number_1, operator, number_2):
    """Функция для обработки знаков вычисление"""

    if operator == "+":
        start.plus(number_1, number_2)
    elif operator == "-":
        start.minus(number_1, number_2)
    elif operator == "*":
        start.multiply(number_1, number_2)
    elif operator == "/":
        start.divide(number_1, number_2)
    else:
        raise UnknownOperator("Неизвестный оператор, попробуйте снова!")

    return start.last_memory


def check_data(data):

    # Проверка на очистку памяти

    if data[0] in ["ce", "c"]:
        print("Очистили память\n")
        start.last_memory = 0
        return

    # TODO можно проще
    if len(data) == 2:
        number_1 = start.last_memory
        number_2 = data[-1]
        operator = data[-2]
    elif len(data) == 3:
        number_1 = data[0]
        number_2 = data[-1]
        operator = data[-2]
    else:
        raise WrongInput("Ошибка ввода данных")

    # Конвертации в данных
    number_1 = Decimal(number_1)
    number_2 = Decimal(number_2)

    start.last_memory = computation(number_1, operator, number_2)
    print("Полученное значение:", start.last_memory)


def main():
    while True:
        data = input("Введите выражение: ").lower()
        data = data.strip().split(" ")

        try:
            check_data(data)
        except UnknownOperator as e:
            print(f"Ошибка: {e}\n")
        except WrongInput as e:
            print(f"Ошибка: {e}\n")
        except InvalidOperation:
            print("Ошибка при конвертации данных в Decimal\n")



if __name__ == '__main__':
    main()
