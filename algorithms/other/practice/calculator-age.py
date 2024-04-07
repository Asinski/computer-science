def find_age(birth_date, birth_month, birth_year, current_date, current_month, current_year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if birth_date > current_date:
        current_month -= 1
        current_date += month[birth_month - 1]
    if birth_month > current_month:
        current_year -= 1
        current_month += 12
    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    print("\nТвой точный текущий возвраст")
    print(calculated_year, calculated_month, calculated_date)


birth_date, birth_month, birth_year = map(int, input("Введи дату своего дня рождения (через пробел).\n").split())
current_date, current_month, current_year = map(int, input("Введите сегодняшнюю дату (через пробел).\n").split())
find_age(birth_date, birth_month, birth_year, current_date, current_month, current_year)
