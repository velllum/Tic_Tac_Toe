

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

    print(all_options)
    print(all_options[::3])
    print(all_options[1::3])
    print(all_options[2::3])

    # Список с положительными вариантами
    positive_options = [  # применить срезы
        # по диагонали
        ["a1", "b2", "c3"],
        ["a3", "b2", "c1"],
        # по вертикали
        ["a1", "a2", "a3"],
        ["b1", "b2", "b3"],
        ["c1", "c2", "c3"],
        # по горизонтали
        ["a1", "b1", "c1"],
        ["a2", "b2", "c2"],
        ["a3", "b3", "c3"],
    ]

    # Список с выбывшими ходами
    exc_steps = []

    # игрок один
    player_1 = None  # Сортировать

    # игрок второй
    player_2 = None

    # чея очередь
    queue = None


def template(steps):
    """- шаблон сетки"""
    string = """
    
         a.  b.  c.
       
    1.   0 | 0 | X
        ---+---+---
    2.   0 | 0 | 0
        ---+---+---
    3.   0 | 0 | 0
    
    """.format(*steps)
    return string


def is_finish():
    pass


def is_victory():
    """- проверка победы"""
    # комбинации вариантов победы
    pass


def is_taken(step, lis):
    """- проверка на пустоту ячейки сетки"""
    if step in lis:
        return False
    return True


def main():
    """- точка входа"""
    while True:
        print(template([]))
        init()
        break


if __name__ == '__main__':
    main()

