'''
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.'''

def foo(n):
    a = 0
    b = 1
    start = a
    while (start < n):
        yield start
        a = b
        b = start
        start = a + b

for number in foo(10):
    print(number, end=' ')