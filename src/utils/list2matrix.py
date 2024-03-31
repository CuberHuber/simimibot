

def list2matrix(_list: list, columns: int) -> list[list]:
    """
    Функция для трансформации списка в матрицу с указанным числом колонок
    :param _list:
    :param columns:
    :return:
    """
    assert isinstance(columns, int) and columns > 0
    assert isinstance(_list, list)

    return [_list[i * columns:(i + 1) * columns] for i in range((len(_list) + columns - 1) // columns)]

