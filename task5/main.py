'''
Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
'''
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Strategy):
    def execute(self, a, b):
        return a + b


class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b


class Calculator:
    def __init__(self, strategy=None):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if self._strategy:
            return self._strategy.execute(a, b)
        else:
            return('Стратегия не установлена')


calc = Calculator()
calc.set_strategy(Addition())
print(calc.calculate(2, 3))
