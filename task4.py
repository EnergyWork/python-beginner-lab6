import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.transforms import offset_copy 
import numpy as np

"""
Нарисовать звёздочками зелёного цвета график кардиоиды в полярной системе координат. 
Добавьте легенду с заголовком «Функция» и подписью «Кардиоида» в левый верхний угол.
Угол принадлежит промежутку от 0 до 3π/2, r = 2,5. 
Уравнение кардиоиды: ρ = 2*r*(1 + cosφ).
"""

def cardioids(phi):
    return 2 * r * (1 + np.cos(phi))

rads = np.arange(0, 3 * np.pi / 2, 0.1) # 3 * np.pi / 2
r = 2.5
arr = []
for radian in rads:
    radius = cardioids(radian)
    arr.append(radius)
plt.polar(rads, arr, '*', color='g')

plt.legend(['Кардиоида'], loc='upper left')
plt.title('Функция')
plt.show()
