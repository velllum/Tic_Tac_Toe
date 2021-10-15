

def init():
    """- инициализация, подготовка данных"""

    # крестик и нолик
    cross = "X"
    zero = "0"

    # координаты всех клеток с индексов в значении
    count = 0
    cells = {}

    for line in ["1", "2", "3"]:
        for column in ["a", "b", "c"]:
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

    # список ничьей ввода в таблицу
    draw_table = ["*"] * len(cells)

    # переменная значка, пустая
    sign = ""

    return cross, zero, win_cells, steps, cells, data_table, sign, draw_table


def print_template(lst):
    """- напечатать шаблон таблицы"""
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


def revers_str(string):
    """- отобразить строку зеркально"""
    return ''.join(list(reversed(string)))


def get_correct_index(ind, ind_rev):
    """- получить корректный индекс координаты"""
    if ind is None:
        ind = ind_rev
    return ind


def rewrite_table(lst, ind, sign):
    """- перезаписать данные таблицы"""
    lst[ind] = sign
    return lst


def get_coordinates(ind_lst, steps_lst, sign):
    """- получить, проверить введенные координаты ячейки"""
    while True:

        coord = input("Укажите координаты ячейки для ( {0} ): ".format(sign))
        coord_revers = revers_str(coord)

        # проверка введенные координаты на валидность
        if coord in ind_lst or coord_revers in ind_lst:

            # проверка веденные координаты на использование ранее
            if coord not in steps_lst and coord_revers not in steps_lst:
                return coord
            else:
                print("Данная ячейка уже занята: {0}".format(coord))
                print("-" * 50)
        else:
            print("Такой ячейки с координатами не существует: {0}".format(coord))
            print("-" * 50)


def get_sign(cross, zero, sign):
    """- выбрать игроку значок"""

    # если значка нет, то установить его
    if not sign:
        return set_sign(cross, zero)

    # поменять значок на противоположный
    if sign == cross:
        return zero
    return cross


def check_victory_option(lst, steps):
    """- проверка победного варианта"""

    # проверка множества на пустоту
    if not steps:
        return None

    # сопоставить множества
    for win in lst:
        if win.issubset(steps):
            return win


def show_win_table(lst_data, lst_win):
    """- отобразить победные данные в таблицы, переопределить data list"""
    for w in lst_win:
        lst_data[w] = "*"
    return lst_data


def get_busy_steps(lst, items):
    """- получить список координат занятых ячеек, из словаря cells"""
    lst_coord = []

    for key, value in items:
        if value in lst:
            lst_coord.append(key)

    return lst_coord


def check_draw(len_steps, len_cells):
    """- проверка на ничью"""
    if len_steps == len_cells:
        return True
    return False


def main():
    """- реализация"""

    # Логика работы

    # инициализируем реестр
    cross, zero, win_cells, steps, cells, data_table, sign, draw_table = init()

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
        coordinates = get_coordinates(
            ind_lst=cells.keys(),
            steps_lst=get_busy_steps(
                lst=[*steps.get(cross), *steps.get(zero)],
                items=cells.items(),
            ),
            sign=sign,
        )

        # получить корректный индекс координаты
        index_coord = get_correct_index(
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

        # проверка победного варианта
        win_cell = check_victory_option(
            lst=win_cells,
            steps=steps.get(sign),
        )

        # проверка, если данные не пусты игра закончена
        if win_cell:
            print_template(
                lst=show_win_table(
                    lst_data=data,
                    lst_win=win_cell,
                )
            )
            print("=" * 15)
            print("Победили - {0}".format(sign))
            print("=" * 15)
            break

        # если получили ничью
        if check_draw(
                len_steps=len([*steps.get(cross), *steps.get(zero)]),
                len_cells=len(cells)
        ):
            print_template(
                lst=draw_table
            )
            print("=" * 15)
            print("У Вас ничья")
            print("=" * 15)
            break

        # распечатать введенные координаты
        print_template(lst=data)


if __name__ == '__main__':
    try:
        main()
    except:
        print("\nИгра была остановлена")
