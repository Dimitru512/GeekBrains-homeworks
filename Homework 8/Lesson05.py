"""Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""


class Storage:
    """Склад хранит экземпляры класса OfficeEquipment"""

    store_equipment_list = []

    def __init__(self, name):
        self.name = name

    def add_to_storage(self, equipment):
        self.store_equipment_list.append(equipment)
        print(f"На склад добавлен {equipment.make} {equipment.model}")

    def give_to_department(self, equipment, department):
        self.store_equipment_list.remove(equipment)
        department.dep_equipment_list.append(equipment)
        print(f"{department.name} получил со склада {equipment.make} {equipment.model}")

    def __str__(self):
        return f"На складе имеется {len(self.store_equipment_list)} позиций"


class Department:
    dep_equipment_list = []

    def __init__(self, name):
        self.name = name


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


store_1 = Storage("Основной склад")
department_1 = Department("Финансовый отдел")
scan_1 = Scanner("HP", "Scanjet 100", True)


store_1.add_to_storage(scan_1)
store_1.give_to_department(scan_1, department_1)


print(store_1)

# Уверен, что это далеко не самое правильное решение поставленной задачи, но уже не хватает времени на это все
