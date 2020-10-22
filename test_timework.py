import timeit

code_vanilla = '''
counter = 0
number = 97
numbers = []
while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers.append(number)
    counter += 1
'''
# print(timeit.timeit(stmt=code_vanilla, number=100))

setup_code = '''
import numpy as np
'''
code_numpy = '''
counter = 0
number = 97
numbers = np.array([])
while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers = np.append(numbers, number)
    counter += 1
'''
# print(timeit.timeit(setup=setup_code, stmt=code_numpy, number=100))

setup_code_npmax = '''
import numpy as np
counter = 0
number = 97
numbers = []
while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers.append(number)
    counter += 1
'''

code_npmax = '''
t = np.max(numbers)
'''
code_max_vanilla = '''
t = max(numbers)
'''
# print(timeit.timeit(setup=setup_code_npmax, stmt=code_npmax, number=100))
# print(timeit.timeit(setup=setup_code_npmax, stmt=code_max_vanilla, number=100))

# TASK NEEDED 
code_vanilla_with_exception = '''
counter = 0
number = '97'
try:
    number = int(number)
except Exception as e:
    raise ValueError('Was entered is not number')
numbers = []
while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers.append(number)
    counter += 1
'''
print(timeit.timeit(stmt=code_vanilla, number=1000))

code_vanilla_without_exception = '''
counter = 0
number = 97
numbers = []
while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    numbers.append(number)
    counter += 1
'''
print(timeit.timeit(stmt=code_vanilla_without_exception, number=1000))
