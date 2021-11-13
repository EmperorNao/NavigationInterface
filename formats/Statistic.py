from formats.Format import Format
from datetime import date
from datetime import time
import pyqtgraph
from math import modf
import numpy as np


class Statistic(Format):
    """
    Class which represent GLOSPASE SGK-T format
    """

    def __init__(self):
        self.name = "Statistic"
        self.matrixes = ["COV_MATRIX", "REV_SKO", "COR_MATRIX"]
        self.arrays = ["MEAN", "SKO", "FAKE_SKO", "More than 3 sigma"]
        self.keys = ["main", "additional", "difference"]
        self.plot_vars = []
        self.interval = "TIME"

    @staticmethod
    def name():
        """

        :return: format name
        """
        return "Statistic"

    def to_str(self, d: dict = {}) -> str:
        """

        :param d: data to repr
        :return: representation of all information
        """
        out = []
        for k, v in d.items():
            out.append(str(k) + ": ")
            for k_, v_ in v.items():
                out.append(str(k_) + ":\n" + str(v_))
        return "\n".join(out)

    def value(self, s: str = "", f: str = "") -> float:
        """

        :param s: value to convert
        :param f: format of value
        :return: tuple of value and measure
        """
        if s == '':
            raise ValueError

        if f == 'DEVICE_ID':
            raise ValueError
        elif f == 'DATE':
            raise ValueError
        elif f == 'TIME':
            return int(s.hour) * 60 + int(s.minute) + float(s.second) / 60
        elif f == 'LATITUDE':
            return float(s)
        elif f == 'N/S':
            raise ValueError
        elif f == 'LONGITUDE':
            return float(s)
        elif f == 'E/W':
            raise ValueError
        elif f == 'SPEED':
            return int(s)
        elif f == 'COURSE':
            return int(s)
        elif f == 'ALTITUDE':
            return int(s)
        elif f == 'ODOMETER':
            return int(s)
        elif f == 'IO_STATUS':
            return int(s)
        elif f == 'EVENT_ID':
            return int(s)
        elif f == 'AIN1':
            return float(s)
        elif f == 'AIN2':
            return float(s)
        elif f == 'FIX_MODE':
            return int(s)

    def measure(self, f: str = '') -> str:
        """

        :param f: format of value
        :return: measurement to this format
        """
        pass

    def format(self, s: str, f: str = '') -> float:
        """

        :param s: value in str
        :param f: format of value
        :return:
        """
        if s == '':
            raise ValueError

        if f == 'DEVICE_ID':
            return int(s)
        pass

    def to_format(self, value, f: str = '') -> str:
        """

        :param value: value
        :param f: format of value
        :return: value for format in string
        """
        if f == '':
            raise ValueError

    def load(self, filename: str = "") -> list:
        """
        :param filename: file which consists rows
        :return: list of dicts
        """

        try:
            info = {}
            with open(filename) as file:

                file = file.readlines()

                i = 0
                cur_info = {}
                cur_format = ""
                while i < len(file):

                    line = file[i]
                    i += 1

                    cleared_line = line.strip("\n").split(":")[0]
                    if cleared_line in self.keys:
                        if cur_format != "":
                            info[cur_format] = cur_info

                        cur_format = cleared_line

                    elif cleared_line in self.arrays:
                        type = cleared_line
                        line = file[i]
                        i += 1
                        cleared_line = line.strip("\n").strip("]").strip("[")
                        arr = np.fromstring(cleared_line, sep=" ")
                        cur_info[type] = arr

                    elif cleared_line in self.matrixes:
                        type = cleared_line
                        matrix = []
                        for row in range(3):
                            line = file[i]
                            i += 1
                            cleared_line = line.strip("\n").strip("]").strip("[")
                            arr = np.fromstring(cleared_line, sep=" ")
                            matrix.append(arr)

                        cur_info[type] = np.array(matrix)

                    else:
                        raise KeyError(f"Wrong format in {filename} file as {self.name} format")

                if cur_format not in info.keys():
                    info[cur_format] = cur_info

        except ValueError as ve:
            raise ve
        except KeyError as ke:
            raise ke

        return info

    def plot(self, format_x, format_y, info: [dict] = [], plotter: pyqtgraph.PlotWidget = None) -> None:
        """
        method to abstract plotting with sense of knowing format and values
        :param format_x:
        :param format_y:
        :param info: data to plot
        :param: plotter: class to plot that provides method plot
        :return:
        """

        try:
            x = [self.value(el[format_x], format_x) for el in info]
            y = [self.value(el[format_y], format_y) for el in info]
            plotter.plot(x, y)
        except KeyError as ke:
            raise ke

    def upload(self, filename: str = "", info: [dict] = []):
        """
        load info to file
        :param filename:
        :param info: data
        :return:
        """

        try:
            with open(filename, mode="w") as file:
                for key, value in info.items():
                    file.write(key + ":\n")

                    for m in self.arrays:
                        file.write(m + ":\n")
                        file.write(np.array2string(value[m], precision=6, separator=" ") + "\n")

                    for m in self.matrixes:
                        file.write(m + ":\n")
                        for row in value[m]:
                            file.write(np.array2string(row, precision=6, separator=" ") + "\n")

        except ValueError as ve:
            raise ve
        except KeyError as ke:
            raise ke

        return

    def __str__(self, d: dict = {}) -> str:
        """

        :param d: data to repr
        :return: representation of all information
        """
        out = []
        for k, val in d.items():
            out.append(str(k) + ": " + str(val))
        return "\n".join(out)
