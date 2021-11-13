from formats.Format import Format
import datetime as dt
from datetime import date
from datetime import time
from datetime import datetime
import pandas as pd
import pyqtgraph
from math import modf


class ETK(Format):
    """
    Class which represent GLOSPASE SGK-T format
    """

    def __init__(self):
        self.name = "ETK"
        self.keys = ["Время", "Скорость", "Координаты"]#, "Положение"]
        self.plot_vars = ['TIME', 'DATE', 'DATETIME', 'SPEED', 'LONGITUDE', 'LATITUDE']
        self.plot_stat = []
        self.interval = "DATETIME"

    @staticmethod
    def name():
        """

        :return: format name
        """
        return "ETK"

    def to_str(self, d: dict = {}) -> str:
        """

        :param d: data to repr
        :return: representation of all information
        """
        out = []
        for k, v in d.items():
            out.append(str(k) + ": " + str(v))
        return "\n".join(out)

    def value(self, s: str = "", f: str = "") -> float:
        """

        :param s: value to convert
        :param f: format of value
        :return: tuple of value and measure
        """
        if s == '':
            raise ValueError("Empty str was provided for value")

        elif f == 'DATE':
            raise ValueError
        elif f == 'TIME':
            return int(s.hour) * 60 + int(s.minute) + float(s.second) / 60
        elif f == "DATETIME":
            return s
        elif f == 'LATITUDE':
            return float(s)
        elif f == 'LONGITUDE':
            return float(s)
        elif f == 'SPEED':
            return int(s)
        else:
            raise KeyError(f"Wrong parameter provided to value : {f}")

    def measure(self, f: str = '') -> str:
        """

        :param f: format of value
        :return: measurement to this format
        """

        if f == 'DATE':
            return "__"
        elif f == 'TIME':
            return "minute"
        elif f == "DATETIME":
            return "minute"
        elif f == 'LATITUDE':
            return "degree"
        elif f == 'LONGITUDE':
            return "degree"
        elif f == 'SPEED':
            return "km/h"
        else:
            raise KeyError(f"Wrong parameter provided to measure : {f}")

    def format(self, s: str, f: str = '') -> float:
        """

        :param s: value in str
        :param f: format of value
        :return:
        """
        if s == '':
            raise ValueError("Empty str was in format")

        if s == "----":
            raise ValueError("None value in format")

        elif f == 'Время':
            return datetime.combine(date(int(s[0:4]), int(s[5:7]), int(s[8:10])),
                              time(int(s[11:13]), int(s[14:16]), int(s[17:19])))
        elif f == 'Координаты':
            spl = s.split(",")
            longitude = float(spl[0].strip(" "))
            latitude = float(spl[0].strip(" "))
            return longitude, latitude

        elif f == 'Скорость':
            return int(s.split(" ")[0])
        else:
            raise KeyError(f"Wrong parameter provided to format : {f}")

    def to_format(self, value, f: str = '') -> str:
        """

        :param value: value
        :param f: format of value
        :return: value for format in string
        """
        pass

    def load(self, filename: str = "") -> list:
        """
        :param filename: file which consists rows
        :return: list of dicts
        """

        c = []
        try:

            df = pd.read_csv(filename, delimiter=";")
            for index, row in df.iterrows():
                d = {}
                try:
                    dtime = self.format(row['Время'], 'Время')
                    longitude, latitude = self.format(row['Координаты'], 'Координаты')
                    speed = self.format(row['Скорость'], 'Скорость')
                    d["DATETIME"] = dtime
                    d["LONGITUDE"] = longitude
                    d["LATITUDE"] = latitude
                    d["SPEED"] = speed
                    c.append(d)
                except:
                    pass

        except ValueError as ve:
            raise ve
        except KeyError as ke:
            raise ke

        return c

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
