# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self):
        print(f"Машина повернута в сторону: {self.name}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 60:
            print("Машина превышает скорость!")


class TownCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.speed}")
        if self.speed > 40:
            print("Машина превышает скорость!")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


sport_car_1 = SportCar(100, "Синий", "Спорткар1", False)
town_car_1 = TownCar(60, "Синий", "Спорткар", False)
work_car_1 = WorkCar(50, "Синий", "Спорткар", False)
police_car_1 = PoliceCar(60, "Синий", "Спорткар", True)

work_car_1.show_speed()
town_car_1.show_speed()
