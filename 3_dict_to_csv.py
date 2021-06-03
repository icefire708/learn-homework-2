"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
from os import write

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    robotyagi = [
        {'name': 'Илон', 'age': 49, 'job': 'Железный человек без костюма'},
        {'name': 'Марк', 'age': 37, 'job': 'Похититель персональных данных'},
        {'name': 'Гвидо', 'age': 65, 'job': 'Бывший диктатор'},
        {'name': 'Павел', 'age': 36, 'job': 'Главный по чатикам'},
    ]
    with open('workers.csv', 'w', encoding='UTF-8', newline='') as f:
        csv_writer = csv.DictWriter(f, robotyagi[0].keys(), delimiter=';')
        csv_writer.writeheader()
        for worker in robotyagi:
            csv_writer.writerow(worker)

if __name__ == "__main__":
    main()
