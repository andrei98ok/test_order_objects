def order_objects_by_color(objects):
    color_mapping = {'К': 3, 'З': 1, 'С': 2}  # Задаем порядок цветов
    sorted_objects = sorted(objects, key=lambda x: color_mapping.get(x, 0))  # Сортируем объекты по порядку цветов
    return sorted_objects

while True:
    # Запрос ввода объектов у пользователя
    input_objects = input("Введите список объектов (буквы С З К без разделителей): ").strip()

    # Преобразуем все буквы в верхний регистр и фильтруем только С, З и К
    filtered_input = ''.join(filter(lambda x: x in ['С', 'З', 'К'], input_objects.upper()))

    # Разделяем отфильтрованные буквы на отдельные объекты
    input_objects = list(filtered_input)

    # Вызываем функцию
    output_objects = order_objects_by_color(input_objects)

    # Выводим сообщение "Результат:" без перевода строки
    print("Результат:", end=" ")

    # Выводим отсортированный набор объектов с пробелами в качестве разделителя
    for obj in output_objects:
        print(obj, end=" ")

    # Переход на новую строку для следующего вывода
    print()

    # Запрос на продолжение или завершение программы
    response = input("Нажмите Enter чтобы ввести новые данные или 'q' для выхода: ")
    if response.lower() == 'q':
        break