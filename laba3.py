import re

digit_to_word = {'0': 'ноль','1': 'один','2': 'два','3': 'три','4': 'четыре',
    '5': 'пять','6': 'шесть','7': 'семь','8': 'восемь','9': 'девять'}

def number_to_words(number): # Преобразует число в строку с названиями цифр
    return ' '.join(digit_to_word[digit] for digit in str(number))

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = re.findall(r'-?\d+', content) # Ищем все целые числа (включая отрицательные)
            filtered_numbers = [] # Фильтруем числа (нечетные и более 3 цифр)
            for num_str in numbers:
                num = int(num_str)
                if num % 2 != 0 and len(num_str.replace('-', '')) > 3:
                    filtered_numbers.append(num)

            print(f"Найденные числа: {filtered_numbers}")
            print(f"Количество чисел: {len(filtered_numbers)}")
            if filtered_numbers:
                print(f"Максимальное число: {max(filtered_numbers)}")
                print(f"Прописью: {number_to_words(max(filtered_numbers))}")
            else:
                print("\nНе найдено подходящих чисел.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
file_path = 'input.txt'
process_file(file_path)
