import matplotlib.pyplot as plt
import os

"""
В каталоге texts сохранить не менее 10 произвольных текстов объемом не менее 500 слов.  
Пользователь программным образом выбирает текст. 
Программа строит график частоты для 50 наиболее частотных слов текста. 
"""

path_to_text = os.getcwd() + '\\texts'
print(path_to_text)

while True:
    number_of_text = input('Enter the number of text (1-10): ')
    try:
        number_of_text = int(number_of_text)
        break
    except ValueError as e:
        print('Was entered the not number')
else:
    if 0 >= number_of_text >= 11:
        print('Out of range')

with open(path_to_text + f'\\{number_of_text}.txt', encoding='utf-8') as f:
    words = f.readline().split()
words_dict = { word : 0 for word in words }
for word in words:
    words_dict[word] += 1
lst = list(words_dict.items())
lst.sort(key=lambda x: x[1], reverse=True)
words_dict = dict(lst)
print(words_dict)
words_dict
data1, data2 = [k for k in words_dict.keys()], [v for v in words_dict.values()]
plt.barh(data1[:51], data2[:51])
plt.title('TOP 50 the most popular words')
plt.show()
