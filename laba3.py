digit_to_word = {'0': 'ноль','1': 'один','2': 'два','3': 'три','4': 'четыре',
    '5': 'пять','6': 'шесть','7': 'семь','8': 'восемь','9': 'девять'}

def number_to_words(number): # Преобразует число в строку с названиями цифр
    return ' '.join(digit_to_word[digit] for digit in str(number))

def extract_numbers(text): # Извлекает целые числа из текста
    numbers = []
    current_number = []
    in_number = False # Флаг: True, если сейчас собираем цифры числа
    for char in text: # Пошаговая обработка каждого символа текста
        if char.isdigit() or (char == '-' and not in_number and not current_number):
            current_number.append(char)
            in_number = True
        else:
            if in_number and current_number:
                numbers.append(int(''.join(current_number)))
                current_number = []
                in_number = False
    if in_number and current_number: # Добавляем последнее число, если текст заканчивается числом
        numbers.append(int(''.join(current_number)))
    return numbers

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = extract_numbers(content)
            filtered_numbers = [] # Фильтруем числа: нечетные и более 3 цифр
            for num in numbers:
                num_str = str(abs(num))
                if num % 2 != 0 and len(num_str) > 3:
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
