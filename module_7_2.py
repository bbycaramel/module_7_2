def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах
            byte_position = file.tell()
            # Записываем строку в файл с добавлением символа новой строки
            file.write(string + '\n')
            # Сохраняем позицию и строку в словаре
            strings_positions[(index, byte_position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
