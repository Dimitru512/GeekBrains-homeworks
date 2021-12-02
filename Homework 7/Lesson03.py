# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
# умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return f"Суммарное количество ячеек равно {self.count + other.count}"

    def __sub__(self, other):
        if self.count - other.count > 0:
            return f"Количество ячеек при вычитании равно {self.count - other.count}"
        else:
            return "В первой клетке меньше ячеек, чем во второй"

    def __mul__(self, other):
        return f"Новая клетка содержит {self.count * other.count} ячеек"

    def __truediv__(self, other):
        return f"Новая клетка содержит {round(self.count / other.count)} ячеек"

    def make_order(self, row):
        return "\n".join(["*" * row for _ in range(self.count // row)]) + "\n" + "*" * (self.count % row)


a = Cell(5)
b = Cell(10)

print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(b / a)
print(a.make_order(2))
