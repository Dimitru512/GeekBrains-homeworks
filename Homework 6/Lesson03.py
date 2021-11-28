# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name: str, surname: str, position: str, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income["wage"]
        self._income_bonus = income["bonus"]


class Position(Worker):
    def get_full_name(self):
        print(f"Работник {self.surname} {self.name} - {self.position}")

    def get_total_income(self):
        print(f"Доход с учетом премии - {self._income_wage + self._income_bonus}")


worker_1 = Position("John", "Doe", "driver", {"wage": 10000, "bonus": 5000})
worker_1.get_full_name()
worker_1.get_total_income()
