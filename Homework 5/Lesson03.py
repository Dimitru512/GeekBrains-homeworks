# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("les3_file.txt", "r") as file:
    salary_sum = 0
    row_count = 0

    print("Сотрудники с окладом менее 20 тысяч:")
    for row in file:
        splited_row = row.split()
        salary_sum += float(splited_row[1])
        if float(splited_row[1]) < 20000:
            print(row)
        row_count += 1

    print(f"Средняя зарплата: {salary_sum / row_count}")
