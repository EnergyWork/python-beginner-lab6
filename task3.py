import matplotlib.pyplot as plt
import numpy as np

"""
Считать данные из текстового документа, в котором написано годовое количество осадков:

Январь 15
Февраль 20
…
Декабрь 11

Вывести их в форме диаграмм: обычная, горизонтальная, круговая (все виды диаграмм должны быть на одном рисунке). Сохранить получившийся рисунок в файл.

"""

def read_file():
    rows = []
    with open('./rainfall.txt', encoding='utf-8') as f:
        rows = f.readlines()
    rows = [pair.split() for pair in rows]
    return [x[0] for x in rows], [x[1] for x in rows]

months, values = read_file()
for m, v in zip(months, values):
    print(m, v)

grid_size = (2, 2)
fig = plt.figure(figsize=(11, 7))
# simple plot
ax1 = plt.subplot2grid(grid_size, (0, 0))
ax1.plot(months, values)
for tick in ax1.get_xticklabels():
    tick.set_rotation(45)
ax1.grid(True)
# horizontal bar
ax2 = plt.subplot2grid(grid_size, (1, 0))
ax2.barh(months, values)
# circular
ax3 = plt.subplot2grid(grid_size, (0, 1), rowspan=2)
ax3.pie(values, labels=months)
# fig params
fig.subplots_adjust(wspace=0.1, hspace=0.3, left=0.11, bottom=0.06, right=0.96, top=0.9)
plt.show()
fig.savefig('temp.png')
