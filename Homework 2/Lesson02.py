# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

new_list = list(input("Введите значения через пробел: ").split())

for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]

print(new_list)

# Почему интерпретатор ругается на строку 9???
