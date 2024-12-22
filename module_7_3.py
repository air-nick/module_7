import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем переданные имена файлов
        self.file_names = file_names

    def get_all_words(self):
        # Создаём словарь для хранения результатов
        all_words = {}

        # Перебираем каждый файл
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем содержимое файла, приводим к нижнему регистру
                    content = file.read().lower()

                    # Убираем пунктуацию
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')

                    # Разбиваем текст на слова
                    words = content.split()

                    # Записываем результат в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, создаём пустой список слов

        return all_words

    def find(self, word):
        # Приводим слово к нижнему регистру для поиска
        word = word.lower()

        # Получаем все слова
        all_words = self.get_all_words()

        # Результат поиска
        result = {}

        # Перебираем файлы и списки слов
        for file_name, words in all_words.items():
            try:
                # Находим индекс первого вхождения слова
                position = words.index(word) + 1  # Смещаем на 1 для "человеческого" счёта
                result[file_name] = position
            except ValueError:
                # Если слово не найдено, ничего не добавляем
                pass

        return result

    def count(self, word):
        # Приводим слово к нижнему регистру для подсчёта
        word = word.lower()

        # Получаем все слова
        all_words = self.get_all_words()

        # Результат подсчёта
        result = {}

        # Перебираем файлы и списки слов
        for file_name, words in all_words.items():
            # Считаем количество вхождений слова
            count = words.count(word)
            result[file_name] = count

        return result


# Тестирование
if __name__ == '__main__':
    finder = WordsFinder('test_file.txt')

    # Все слова
    print(finder.get_all_words())

    # Позиция первого вхождения слова
    print(finder.find('TEXT'))

    # Количество вхождений слова
    print(finder.count('teXT'))
