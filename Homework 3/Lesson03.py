# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """Выводит сумму двух наибольших аргументов"""
    try:
        a, b, c = float(a), float(b), float(c)
        return max(a + b, b + c, a + c)
    except TypeError:
        return "Ошибка ввода данных"
    except ValueError:
        return "Ошибка ввода данных"


val1 = input("Введите первое число: ")
val2 = input("Введите второе число: ")
val3 = input("Введите третье число: ")

print("\nРезультат -> " + str(my_func(val1, val2, val3)))
