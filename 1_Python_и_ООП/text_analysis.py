# Утилита для анализа текста
# -Логировать выполнение функций.
# -Кэшировать результаты анализа.
# -Читать большие текстовые файлы построчно.
# -Подсчитывать частоту слов в тексте.

from collections import Counter

# Декоратор для логирования
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершила выполнение с результатом {result}")
        return result
    return wrapper

# Декоратор для кэширования
def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            print("Результат из кэша")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        print("Результат вычислен")
        return result
    return wrapper

# Генератор для чтения больших файлов
def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# Функция для анализа текста
@logger
@cache
def analyze_text(file_path):
    word_count = Counter()
    for line in read_large_file(file_path):
        words = line.split()
        word_count.update(words)
    return word_count.most_common(10)

# Пример использования
print(analyze_text('ttt.txt'))