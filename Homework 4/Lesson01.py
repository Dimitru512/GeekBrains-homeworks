# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) == 4:
    try:
        hours, rate, premium = map(float, argv[1:])
        print(f"Рабочие часы: {hours}")
        print(f"Выплата в час: {rate}")
        print(f"Премия: {premium}")
        print("\nИтоговая выплата: " + str(hours * rate + premium))
    except ValueError:
        print("Вводимые данные должны быть числами")
else:
    print("Должно быть три аргумента:\n"
          "1) выработка в часах\n"
          "2) ставка в час\n"
          "3) премия")
