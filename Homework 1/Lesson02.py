seconds = int(input("Введите количество секунд: "))

if 0 <= seconds <= 356400:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds %= 60
    print("{:>02}:{:>02}:{:>02}".format(hours, minutes, seconds))
else:
    print("Некорректное значение секунд")
