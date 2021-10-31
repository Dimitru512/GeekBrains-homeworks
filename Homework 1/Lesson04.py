number = int(input("Введите число: "))
max_figure = 0

while number != 0:
    if number % 10 > max_figure:
        max_figure = number % 10
    number //= 10

print(f"Максимальная цифра в числе {max_figure}")
