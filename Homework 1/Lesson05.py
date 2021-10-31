proceeds = int(input("Введите значение выручки: "))
outgoings = int(input("Введие значение издержек: "))

if proceeds > outgoings:
    print("Фирма получила прибыль")
    print("Рентабельность выручки составляет " + str(proceeds / outgoings))
    employees = int(input("Введите количество сотрудников: "))
    print("Прибыль в фирме на одного сотрудника составляет " + str((proceeds - outgoings) / employees))
elif proceeds < outgoings:
    print("Фирма работает в убыток")
else:
    print("Фирма ушла в ноль")
