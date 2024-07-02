# from src.directory import get_parent_dir
# import os
#
# def get_parent_dir(path):
#     """Функция перехода в родительскую директорию"""
#
#     return os.path.abspath(os.path.join(path, os.pardir))
#
# ==========================================================
# В main. Переход в родительский каталог
#
# parent_dir = get_parent_dir(os.path.dirname(__file__))
# with open(parent_dir + r"\data\transactions.txt", "r", encoding='utf-8') as file:
#     content = file.read()
#
# print(content)
