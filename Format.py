# TODO: do not use bare except
from datetime import date
from datetime import time


class Format:

    def __init__(self):
        pass

    @staticmethod
    def name():
        return None

    def value(self, s: str = "", f: str = "") -> float:
        """

        :param s: value to convert
        :param f: format of value
        :return: value
        """
        return None

    def format(self, s: str, f: str = ''):
        """

        :param s: value in str
        :param f: format of value
        :return:
        """
        return None

    def to_format(self, value, f: str = '') -> str:
        """

        :param value: value
        :param f: format of value
        :return: value for format in string
        """

    def convert(self, s: str = '', sep: str = ','):
        return None

    def load(self, filename: str = "") -> [dict]:
        return None

    def plot(self, format_x, format_y) -> tuple:
        return None

    def upload(self, filename: str = ""):
        return
