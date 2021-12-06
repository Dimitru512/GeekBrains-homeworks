"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class Storage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class OfficeEquipment:
    def __init__(self, make, model):
        self.model = model
        self.make = make


class MFP(OfficeEquipment):
    def __init__(self, make, model, print_speed: int):
        super().__init__(make, model)
        self.print_speed = print_speed


class Printer(OfficeEquipment):
    def __init__(self, make, model, duplex_print: bool):
        super().__init__(make, model)
        self.duplex_print = duplex_print


class Scanner(OfficeEquipment):
    def __init__(self, make, model, duplex_scan: bool):
        super().__init__(make, model)
        self.duplex_scan = duplex_scan
