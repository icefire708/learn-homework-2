"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days() -> None:
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    current_moment = datetime.now()
    date_format = '%d.%m.%Y'
    print(f'Сегодня: {current_moment.strftime(date_format)}')
    last_day = current_moment - timedelta(days=1)
    print(f'Вчера: {last_day.strftime(date_format)}')
    thirty_days_ago = current_moment - timedelta(days=30)
    print(f'30 дней назад: {thirty_days_ago.strftime(date_format)}')


def str_2_datetime(date_string: str) -> datetime:
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
