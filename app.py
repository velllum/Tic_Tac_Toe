

def init():
    """- инициализируем данные"""

    # переменные с крестиком и ноликом
    cross = "X"
    zero = "O"

    # наименование строк
    lines = ["1", "2", "3"]

    # наименование столбцов
    columns = ["a", "b", "c"]

    # все варианты ходов
    all_options = [
        column + line
        for line in lines
        for column in columns
    ]

    # Список с положительными вариантами
    positive_options = [
        # по диагонали
        ["a1", "b2", "c3"], ["a3", "b2", "c1"],

        # получить вертикальные варианты
        *[all_options[i::3] for i in range(3)],

        # получить горизонтальные варианты
        *[all_options[i:i+3] for i in range(0, 7, 3)]
    ]

    # Список с выбывшими ходами
    exc_steps = []

    # игрок один
    player_1 = []  # Сортировать .sort()

    # игрок второй
    player_2 = []

    # хранить очередь
    queue = None

    return cross, zero, lines, positive_options, exc_steps, player_1, player_2, queue


def template(steps):
    """- шаблон сетки"""
    if not steps:
        steps = [" "]*9

    string = """
    
         a.  b.  c.

    1.   {0} | {1} | {2}
       ----+---+----
    2.   {3} | {4} | {5}
       ----+---+----
    3.   {6} | {7} | {8}
    
    """.format(*steps)
    return string


def is_finish():
    pass


def is_victory(positive_steps, step):
    """- проверка победы"""
    if step in positive_steps:
        return True
    return False


def is_taken(step, lis):
    """- проверка на пустоту"""
    if step in lis:
        return False
    return True


def revers_str(string):
    return ''.join(list(reversed(string)))


def is_step(all_steps, step):
    """- проверка хода на существование"""
    if step in all_steps:
        return True

    elif revers_str(step) in all_steps:
        return True

    return False


def main():
    """- точка входа"""
    while True:
        print(template([]))
        print(template(list(range(10))))
        init()
        break


if __name__ == '__main__':
    main()

