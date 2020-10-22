import numpy as np
import matplotlib
import timeit

"""
Реализовать последовательность Коллатца с проверкой, что пользователь ввел число. 
На выводе указать за какое количество шагов получили единичку и какое максимальное число получали в процессе. 
Выполнить замер времени работы кода без обработки исключений и с ней.
"""

number = input('Enter the some number: ')
try:
    number = int(number)
except Exception as e:
    raise ValueError('Was entered is not number')

counter = 0
numbers = []

while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers.append(number)
    counter += 1

print(numbers)
print('Count of steps:', counter)
print('Maximum number:', max(numbers))
