def custom_write(file_name, strings):
    """
    Записывает строки из списка strings в файл file_name и возвращает словарь с позициями строк.

    :param file_name: str - имя файла для записи
    :param strings: list - список строк для записи
    :return: dict - словарь строк с их позициями
    """
    # Словарь для хранения информации о строках
    strings_positions = {}

    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах
            byte_position = file.tell()

            # Записываем строку в файл с переходом на новую строку
            file.write(string + '\n')

            # Сохраняем информацию о строке в словарь
            strings_positions[(line_number, byte_position)] = string

    # Возвращаем результат
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test_7_2.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)
