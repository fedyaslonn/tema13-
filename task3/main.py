'''
Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
'''

class Pizza:

    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

class PizzaBuilder(Pizza):

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self, cheese):
        self.cheese = cheese
        return self

    def add_pepperoni(self, pepperoni):
        self.pepperoni = pepperoni
        return self

    def add_mushrooms(self, mushrooms):
        self.mushrooms = mushrooms
        return self

    def add_onions(self, onions):
        self.onions = onions
        return self

    def add_bacon(self, bacon):
        self.bacon = bacon
        return self


class PizzaDirector(PizzaBuilder):

    def make_pizza(self, size):
        return self.add_bacon().add_cheese()

pizza = Pizza("Large", True, True, False, False, True)
director = PizzaDirector()
director.make_pizza()