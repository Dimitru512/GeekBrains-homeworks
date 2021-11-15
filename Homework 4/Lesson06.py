# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from sys import argv
from itertools import count, cycle

# Итератор 1

try:
    if int(argv[1]) >= 15:
        print("Введите число меньше 15")
    else:
        start_num = int(argv[1])
        for num in count(start_num):
            print(num)
            if num >= 15:
                break
except ValueError:
    print("Нужно ввести целое число")

# Итератор 2

# counter = 0
#
# for el in cycle(argv[1]):
#     print(el)
#     counter += 1
#     if counter >= 10:
#         break