seconds = int(input("Введите количество секунд: "))

if 0 <= seconds <= 356400:
    minutes = seconds % 60
    hours = seconds // 3600
    seconds %= 60
    print("{:>02}:{:>02}:{:>02}".format(hours, minutes, seconds))
else:
    print("Некорректное значение секунд")
