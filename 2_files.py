"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r') as f:
        file_text = f.read()
    print(f'Количество символов в файле: {len(file_text)}')
    words_count = 0
    current_word_len = 0
    for character in file_text + '!':
        if character.isalpha():
            current_word_len += 1
        else:
            if current_word_len:
                words_count += 1
            current_word_len = 0
    print(f'Количество слов в файле: {words_count}')
    file_text = file_text.replace('.', '!')
    with open('referat2.txt', 'w') as f:
        f.write(file_text)

if __name__ == "__main__":
    main()
