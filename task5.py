import matplotlib.pyplot as plt
import numpy as np

"""
Написать программу изображения графика функции y=√x. Не забывайте про то, что функция имеет значения ≥ 0. 
Предварительно программа запрашивает у пользователя следующую информацию:
    - цвет графика (программа предлагает не менее пяти различных цветов);
    - тип линии (программа предлагает не менее трех различных вариантов); 
    - толщину линии (программа предлагает не менее пяти различных вариантов).
Все запросы к пользователю обрабатываются с использованием обработки исключительных ситуаций.
Варианты можно вводить строкой или числом (на ваш выбор).
"""

def func(x):
    return np.sqrt(x)

# linestyle: - -. : --
# color: red green blue black yellow
# linewidth: 1 1.2 1.4 1.6 1.8 2

user_color_dict = { 'red':0, 'green':1, 'blue':3, 'black':4, 'yellow':5 }
while True:
    user_color = input('Введите нужный цвет (red green blue black yellow) > ')
    try:
        index = user_color_dict[user_color]
        break
    except KeyError as e:
        print('Цвет не доступен')

user_linestyle_dict = { '-':0, '-.':1, ':':1, '--':3 }
while True:
    user_linestyle = input('Введите нужный тип линии (- -. : --) > ')
    try:
        index = user_linestyle_dict[user_linestyle]
        break
    except KeyError as e:
        print('Недействительный тип линии')

while True:
    user_linewidth = input('Введите толщину линии > ')
    try:
        user_linewidth = float(user_linewidth)
        if user_linewidth <= 0:
            print('Число меньше нуля')
        else:
            break
    except ValueError as e:
       print('Недействительный тип линии')

values = [func(x) for x in np.arange(0, 10, 0.1)]
plt.plot(values, color=user_color, linestyle=user_linestyle, linewidth=user_linewidth)
plt.grid(True)
plt.title('y = sqrt(x)')
plt.show()
