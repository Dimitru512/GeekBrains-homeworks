# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("les1_file.txt", "w") as file:
    x = None
    print("Для выхода оставьте поле ввода пустым и нажмите Enter")
    while x != "":
        x = input("Введите текст: ")
        file.write(x + "\n")
