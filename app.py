

def init():
    """- инициализируем данные"""

    # крестик и нолик
    cross = "X"
    zero = "0"

    # координаты всех клеток с индексов в значении
    count = 0
    cells = {}

    for column in ["a", "b", "c"]:
        for line in ["1", "2", "3"]:
            cells[column + line] = count
            count += 1

    # положительные варианты ходов
    win_cells = [
        {0, 4, 8}, {2, 4, 6},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    ]

    # словарь с ходами игроков
    steps = {
        cross: set(),
        zero: set(),
    }

    # пустой список с данными ввода в таблицу
    data_table = [" "] * len(cells)

    # переменная значка, пустая
    sign = ""

    return cross, zero, win_cells, steps, cells, data_table, sign


def print_template(lst):
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
    print(string)


def set_sign(cross, zero):
    """- Выбор знака"""
    while True:
        result = input("Укажите значок для игры - X или 0: ")
        if result == cross or result == zero:
            return result
        else:
            print("Вы указали не верные данные")


def is_victory(steps, win_lst):
    """- проверка победного варианта"""
    for win in win_lst:
        if win.issubset(steps):
            return win
        return False


def revers_str(string):
    """- отразить строку зеркально"""
    return ''.join(list(reversed(string)))


def get_ind_coord(ind, ind_rev):
    """- получить индекс координаты"""
    if not ind:
        ind = ind_rev
    return ind


def rewrite_table(lst, ind, sign):
    """- перезаписать данные таблицы"""
    lst[ind] = sign
    return lst


def get_coord(ind_lst, steps_lst, sign):
    """- получить введенные координаты ячейки"""
    while True:

        coord = input("Укажите координаты ячейки - {0}: ".format(sign))

        # проверка введенные координаты на валидность
        if coord in ind_lst or revers_str(coord) in ind_lst:

            # проверка веденные координаты на использование ранее
            if coord not in steps_lst:
                return coord
            else:
                print("Данная ячейка уже занята: {0}".format(coord))
                print("-" * 50)
        else:
            print("Такой ячейки с координатами не существует: {0}".format(coord))
            print("-" * 50)


def get_sign(cross, zero, sign):
    """- выбрать игроку значок"""
    if not sign:
        return set_sign(cross, zero)

    # поменять значок на противоположный
    if sign == cross:
        return zero
    return cross


def main():
    """- реализация"""

    # Логика работы

    # инициализируем реестр
    cross, zero, win_cells, steps, cells, data_table, sign = init()

    # Распечатать пустую таблицу
    print_template(data_table)

    print("Для выбора клетки укажите ее координаты a1 или 1a, смотрите таблицу выше.")
    print("=" * 50)

    while True:

        # поменять значок на противоположный, второго игрока
        sign = get_sign(
            cross=cross,
            zero=zero,
            sign=sign,
        )

        # получить координаты ячейки
        coordinates = get_coord(
            ind_lst=cells.keys(),
            steps_lst=[*steps.get(cross), *steps.get(zero)],
            sign=sign,
        )

        # получить индекс координаты
        index_coord = get_ind_coord(
            ind=cells.get(coordinates),
            ind_rev=cells.get(revers_str(coordinates)),
        )

        # перезаписать таблицу
        data = rewrite_table(
            lst=data_table,
            ind=index_coord,
            sign=sign,
        )

        # добавить индекс в список текущего игрока, с выбранным значком
        steps[sign].add(index_coord)


        # распечатать введенные координаты
        print_template(data)


        #
        # # проверка победителя
        # if is_victory(lst_cross, win_cells):
        #     print("Победили: ", sign)
        #
        # if is_victory(lst_zero, win_cells):
        #     print("Победили: ", sign)

        break


if __name__ == '__main__':
    main()
