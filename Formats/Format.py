# TODO: do not use bare except
from datetime import date
from datetime import time

import pyqtgraph


class Format:
    """
    Interface that provides all methods which new formats must define
    """
    def __init__(self):
        # all variables in format
        self.keys = []
        # plottable variables in format
        self.plot_vars = []
        self.plot_stat = []
        pass

    def var_keys(self):
        """

        :return: all variables in format
        """
        return self.keys

    def plot_keys(self):
        """

        :return: all plottable variables
        """
        return self.plot_vars

    def to_str(self, d: dict = {}) -> str:
        """

        :param d: data to repr
        :return: representation of all information
        """
        return None

    @staticmethod
    def name():
        """

        :return: format name
        """
        return None

    def value(self, s: str = "", f: str = "") -> float:
        """
        get value as number for current format
        :param s: value to convert
        :param f: format of value
        :return: value as number
        """
        return None

    def measure(self, f: str = '') -> str:
        """

        :param f: format of value
        :return: measurement to this format
        """

    def format(self, s: str, f: str = ''):
        """
        convertion from format to internal python storing
        :param s: value in str
        :param f: format of value
        :return: value in correct type to store
        """
        return None

    def to_format(self, value, f: str = '') -> str:
        """
        reverse format method, convertion from python storing into format
        :param value: value
        :param f: format of value
        :return: value for format in string
        """

    def convert(self, s: str = '', sep: str = ',') -> dict:
        """
        convert one line from file
        :param s: line
        :param sep: separator
        :return: return dict of storing in line values
        """
        return None

    def load(self, filename: str = "") -> [dict]:
        """
        load info from file
        :param filename:
        :return: list of dicts values
        """
        return None

    def plot(self, format_x, format_y, info: [dict] = [], plotter: pyqtgraph.PlotWidget = None) -> tuple:
        """
        method to abstract plotting with sense of knowing format and values
        :param format_x:
        :param format_y:
        :param info: data to plot
        :param: plotter: class to plot that provides method plot
        :return:
        """
        return None

    def upload(self, filename: str = "", info: [dict] = []):
        """
        load info to file
        :param filename:
        :param info: data
        :return:
        """
        return
