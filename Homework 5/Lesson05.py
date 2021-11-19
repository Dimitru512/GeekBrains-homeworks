# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randrange

with open("les5_file.txt", "w") as file:
    my_list = [str(randrange(0, 10)) for i in range(0, 10)]
    file.write(" ".join(my_list))
    print(f"В файл les5_file.txt записаны числа: {' '.join(my_list)}")

with open("les5_file.txt") as file:
    new_list = map(int, file.read().split())
    print(f"Сумма чисел из файла les5_file.txt равна {sum(new_list)}")
