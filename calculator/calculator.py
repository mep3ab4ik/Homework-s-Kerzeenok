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
отдельный метод. Итого должно быть 5 методов класса калькулятора, включая конструктор.

"""
from error import WrongInput
from decimal import Decimal

class Calculator:

    def __init__(self):

        self.last_memory: int | Decimal = 0


    def plus(self, first, second) -> int:
        """Метод сложение чисел"""

        self.last_memory = first + second
        return self.last_memory


    def minus(self, first, second) -> int:
        """Метод вычитания чисел"""

        self.last_memory = first - second
        return self.last_memory


    def multiply(self, first, second) -> int:
        """Метод умножение чисел"""

        self.last_memory = first * second
        return self.last_memory

    def divide(self, first, second) -> int:
        """Метод деление чисел"""
        if second == 0:
            raise WrongInput("Делить на '0' нельзя")
        self.last_memory = first / second
        return self.last_memory

