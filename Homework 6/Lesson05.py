# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки " + self.title)


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой " + self.title)


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом " + self.title)


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером " + self.title)


pen_1 = Pen("Синяя ручка")
pen_1.draw()
pencil_1 = Pencil("Зеленый карандаш")
pencil_1.draw()
handle_1 = Handle("Черный маркер")
handle_1.draw()
