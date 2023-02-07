class FlatIterator:

    # определяет атрибут для хранения списка списков
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    # определяет атрибуты для итерации по списку
    def __iter__(self):
    # определяем итератор для списка
        self.list_iter = iter(self.list_of_list)
    # определяем вложенный список для добавления элементов
        self.nested_list = []
    # смещаем курсор за границу списка
        self.cursor = -1
        return self

    # определяет и возвращает следущий элемент списка списков
    def __next__(self):
        self.cursor += 1
    # если курсор в конце вложенного списка, то список и курсор обнуляем
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
    # если вложенные списки закончились, то получаем stop iteration
            while not self.nested_list:
    # если  список пустой, то получаем следующий вложенный список
                self.nested_list = next(self.list_iter)
        return self.nested_list[self.cursor]

    #генератор позволяет  возвращать эелементы из списка списков с двойным уровнем вложености
def flat_generator(my_list):
   for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('~ ' * 8)
    print('Вызов итератора')
    for item in FlatIterator(nested_list):
        print(item)
    print(' ~' * 8)

    print('- ' * 8)
    print('Вызов list comprehension')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print(' -' * 8)
    print()
    print('# ' * 8)
    print('Вызов генератора')
    for item in flat_generator(nested_list):
        print(item)
    print(' #' * 8)