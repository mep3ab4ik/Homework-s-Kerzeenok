"""Давай калькулятор делать со звездочкой)

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

from calculator import Calculator
from decimal import Decimal
def main():
    """"""
    # Переменная со всеми операторами

    operators = {"+", "-", "*", "/"}

    # Первое число и последней вывод

    start = Calculator()

    while True:
        # Индекс для чисел
        index = 0

        data = input("Введите выражение: ").lower()

        #Стоп программы

        if data == "stop":
            exit()

        # Проверка на очистку памяти

        if data == "c" or data == "ce":
            print("Очистили память")
            start.last_memory = 0
            continue

        # Поиск оператора
        # for i in data:
        #     if i in operators:





        # Поиск и запись числа, оператора в переменные
        for i in data:
            if i in operators:
                number_1 = data[:index].strip()
                number_2 = data[index+1:].strip()
                operator = i
            index += 1

        # print(number_1)
        # print(number_2)
        # print(operator)


        # Проверка на полное выражение или '+ number'

        if not number_1:
            number_1 = start.last_memory

        # TODO Конвертируем в формат int
        number_1 = Decimal(number_1)
        number_2 = Decimal(number_2)

        if operator == "+":
            start.plus(number_2, number_1)

        if operator == "-":
            start.minus(number_2, number_1)

        if operator == "*":
            start.multiply(number_2, number_1)

        if operator == "/":
            start.divide(number_2, number_1)

        print("Получилось значение:", start.last_memory)



if __name__ == '__main__':
    main()
