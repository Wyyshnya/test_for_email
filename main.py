import argparse
import json


class UniqueListFromJSON:
    def __init__(self):
        self.unique_elements = []

    def get_unique_elements(self, data):
        # Если приходящий элемент словарь
        if isinstance(data, dict):
            # Начинаем перебор по ключам
            for element in data:
                # Если ключа нет в списке, то сразу добавляем его в список уникальных значений
                if not (element in self.unique_elements):
                    self.unique_elements.append(element)
                # Если значение ключа словарь или список - запускаем рекурсию
                if isinstance(data[element], dict) or isinstance(data[element], list):
                    self.get_unique_elements(data[element])

                # Если значение ключа не список и не словарь,
                # то есть str или int, добавляем его в список уникальных значений
                else:
                    if not (data[element] in self.unique_elements):
                        self.unique_elements.append(data[element])
        # Если приходящий элемент список
        elif isinstance(data, list):
            # Начинаем перебор элементов в списке
            for element in data:
                # Если элемент список или словарь - запускаем рекурсию
                if isinstance(element, dict) or isinstance(element, list):
                    self.get_unique_elements(element)

                # Если значение ключа не список и не словарь,
                # то есть str или int, добавляем его в список уникальных значений
                else:
                    if not (element in self.unique_elements):
                        self.unique_elements.append(element)

    def __repr__(self):
        # Выводит массив уникальных элементов
        return self.unique_elements


def parse(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            manager = UniqueListFromJSON()
            manager.get_unique_elements(data)
            print(manager.__repr__())
    except FileNotFoundError:
        print('Неправильно указан файл или путь к нему')


if __name__ == '__main__':
    # Добавляем аргумент для парсинга пути к файлу из консоли
    parser = argparse.ArgumentParser(description='Path to the json.file')
    parser.add_argument('-p', '--path', type=str, help='Path to the json.file')

    args = parser.parse_args()
    if args.path is not None:
        parse(args.path)
    else:
        print("Не указан путь к файлу")
