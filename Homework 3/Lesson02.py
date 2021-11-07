# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, city, email, phone):
    """Выводит аргументы в одну строку через пробел"""
    return f"{name} {surname} {birth_year} {city} {email} {phone}"


print("Введите данные\n")

print("\nВведенные данные о пользователе: " +
      user_data(name=input("Введите имя: "),
                surname=input("Введите фамилию: "),
                birth_year=input("Введите год рождения: "),
                city=input("Введите город: "),
                email=input("Введите email: "),
                phone=input("Введите телефон: ")
                ))
