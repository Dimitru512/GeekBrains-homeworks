# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]

print(f"Текущий рейтинг {rating_list}")  # Проверку на натуральные чила не стал делать

new_value = int(input("Введите новое натуральное значение: "))
if min(rating_list) > new_value:
    rating_list.append(new_value)
else:
    for i in range(0, len(rating_list)):
        if new_value >= rating_list[i]:
            rating_list.insert(i, new_value)
            break
print(f"Новый рейтинг: {rating_list}")
