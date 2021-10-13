
def init():
    """- инициализируем данные"""

    # крестик и нолик
    cross = "X"
    zero = "0"

    # строки
    lines = ["1", "2", "3"]

    # столбцы
    columns = ["a", "b", "c"]

    # клетки - наименование и индекс
    count = 0
    cells = {}

    for column in columns:
        for line in lines:
            cells[column + line] = count
            count += 1

    # положительные варианты
    win_cells = [
        [0, 4, 8], [2, 4, 6],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 1, 2], [3, 4, 5], [6, 7, 8]
    ]

    # занятые клетки нолика
    lst_0 = []  # Сортировать .sort()

    # занятые клетки крестика
    lst_x = []

    # Список с выбывшими клетками
    exc_cells = []

    return cross, zero, win_cells, lst_x, lst_0, exc_cells, list(cells.keys()), cells


def template(lst):
    """- шаблон сетки"""
    string = """
    
          a.   b.   c.
       +---------------+
    1. |  {0} |  {1}  | {2}  |
       |----+-----+----|
    2. |  {3} |  {4}  | {5}  |
       |----+-----+----|
    3. |  {6} |  {7}  | {8}  |
       +---------------+
    """.format(*lst)
    return string


def set_sign():
    """- Выбор знака"""
    while True:
        result = input("Укажите значок для игры - X или 0: ")
        if result == "X" or result == "0":
            return result
        else:
            print("Вы указали не верные данные")


def is_victory(lst, win_lst):
    """- проверка победного варианта"""
    if lst in win_lst:
        return True

    return False


def revers_str(string):
    """- отразить строку зеркально"""
    return ''.join(list(reversed(string)))


def cell_employed(lst, sign):
    """- проверка на использование координат раннее"""
    if sign not in lst or revers_str(sign) not in lst:
        return True

    return False


def cell_valid(lst, sign):
    """- Проверка введенных координат на существование"""
    if sign in lst:
        return True

    return False


def is_cell(exc_lst, coord_cells, sign):
    """- проверка введенные координаты на валидность"""
    while True:
        input_sign = input("Укажите координаты ячейки - {0}: ".format(sign))

        if cell_valid(coord_cells, input_sign):
            if cell_employed(exc_lst, input_sign):
                return input_sign

            print("Вы указали координаты уже занятой ячейки: {0}".format(input_sign))

        else:
            print("Вы указали не существующие координаты: {0}".format(input_sign))


def main():
    """- реализация"""

    # Логика работы

    # пустой список с данными ввода в клетки
    result = [" "] * 9

    # указать знак игрока X или 0
    sign = set_sign()

    # Распечатать пустую таблицу
    print(template(result))

    print("Для выбора клетки укажите ее координаты a1 или 1a, смотрите таблицу выше.")

    print("="*50)

    # инициализируем реестр
    cross, zero, win_cells, lst_cross, lst_zero, exc_cells, coord_cells, cells = init()

    while True:

        # проверка валидности ячейки
        input_sign = is_cell(exc_cells, coord_cells, sign)

        # добавить валидные данные в список примененных клеток
        exc_cells.append(input_sign)

        # введенные координаты добавляем в список result
        ind = cells.get(input_sign)
        result[ind] = sign

        # распечатать введенные координаты
        print(template(result))

        # добавить данные в список значка
        if sign == cross:
            lst_cross.append(input_sign)

        elif sign == zero:
            lst_zero.append(input_sign)

        # проверка победителя
        if is_victory(lst_cross, win_cells):
            print("Победили: ", sign)

        if is_victory(lst_zero, win_cells):
            print("Победили: ", sign)


if __name__ == '__main__':
    main()
