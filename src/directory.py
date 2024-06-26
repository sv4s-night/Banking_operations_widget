import os


def get_parent_dir(path):
    """Функция перехода в родительскую директорию"""

    return os.path.abspath(os.path.join(path, os.pardir))
