def read_file(filename) -> str:
    """
    Чтение input файла целиком.

    Args:
        filename: Название файла
    """
    with open(filename, 'r') as file:
        content = file.read()
    return content


def read_file_by_line(filename) -> tuple:
    """
    Чтение input файла построчно.

    Args:
        filename: Название файла
    """
    with open(filename, 'r') as file:
        for line in file:
            if line:
                yield line
