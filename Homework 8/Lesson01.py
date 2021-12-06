"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class DateClass:
    day: int
    month: int
    year: int

    def __init__(self, date: str):
        date_num = self.date_to_int(date)
        self.date_validation(date_num)
        self.day, self.month, self.year = date_num

    @classmethod
    def date_to_int(cls, date: str):
        return [int(x) for x in date.split("-")]

    @staticmethod
    def date_validation(num: list):
        d, m, y = num
        if 1 <= d <= 31 and 1 <= m <= 12 and y > 0:
            print("Дата корректна")
        else:
            print("Дата некорректна")


my_date_1 = DateClass("10-12-2003")
my_date_2 = DateClass("10-13-2021")

print(DateClass.date_to_int("10-12-2010"))
