from formats.Format import Format
from datetime import date
from datetime import time
import pyqtgraph
from math import modf


class SgkT(Format):
    """
    Class which represent GLOSPASE SGK-T format
    """

    def __init__(self):
        self.name = "SGK_T"
        self.keys = ['DEVICE_ID', 'DATE', 'TIME', 'LATITUDE', 'N/S', 'LONGITUDE', 'E/W',
                'SPEED', 'COURSE', 'ALTITUDE', 'ODOMETER', 'IO_STATUS', 'EVENT_ID', 'AIN1', 'AIN2',
                'FIX_MODE', ('%s_SAT_NO' % self.name), 'GPS_SAT_NO', 'HDOP']
        self.plot_vars = ['TIME', 'LATITUDE', 'LONGITUDE',
                'SPEED', 'COURSE', 'ALTITUDE', 'HDOP']
        self.plot_stat = []
        self.interval = "TIME"

    @staticmethod
    def name():
        """

        :return: format name
        """
        return "SGK_T"

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
        elif f == ('%s_SAT_NO' % self.name):
            return int(s)
        elif f == 'GPS_SAT_NO':
            return int(s)
        elif f == 'HDOP':
            return float(s)

    def measure(self, f: str = '') -> str:
        """

        :param f: format of value
        :return: measurement to this format
        """

        if f == 'DEVICE_ID':
            return "__"
        elif f == 'DATE':
            return "__"
        elif f == 'TIME':
            return "minute"
        elif f == 'LATITUDE':
            return "degree"
        elif f == 'N/S':
            raise "__"
        elif f == 'LONGITUDE':
            return "degree"
        elif f == 'E/W':
            return "__"
        elif f == 'SPEED':
            return "km/h"
        elif f == 'COURSE':
            return "__"
        elif f == 'ALTITUDE':
            return "__"
        elif f == 'ODOMETER':
            return "__"
        elif f == 'IO_STATUS':
            return "__"
        elif f == 'EVENT_ID':
            return "__"
        elif f == 'AIN1':
            return "__"
        elif f == 'AIN2':
            return "__"
        elif f == 'FIX_MODE':
            return "__"
        elif f == ('%s_SAT_NO' % self.name):
            return "__"
        elif f == 'GPS_SAT_NO':
            return "__"
        elif f == 'HDOP':
            return "__"
        else:
            raise ValueError

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
        elif f == 'DATE':
            return date(int('20' + s[4:6]), int(s[2:4]), int(s[0:2]))
        elif f == 'TIME':
            return time(int(s[0:2]), int(s[2:4]), int(s[4:6]))
        elif f == 'LATITUDE':
            return int(s[0:3]) + float(s[3:]) / 60
        elif f == 'N/S':
            return s
        elif f == 'LONGITUDE':
            return int(s[0:3]) + float(s[3:]) / 60
        elif f == 'E/W':
            return s
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
        elif f == ('%s_SAT_NO' % self.name):
            return int(s)
        elif f == 'GPS_SAT_NO':
            return int(s)
        elif f == 'HDOP':
            return float(s)

    def to_format(self, value, f: str = '') -> str:
        """

        :param value: value
        :param f: format of value
        :return: value for format in string
        """
        if f == '':
            raise ValueError

        if f == 'DEVICE_ID':
            return str(value)
        elif f == 'DATE':
            return \
                str(int(value.day)).rjust(2, '0') + \
                str(int(value.month)).rjust(2, '0') + \
                str(int(value.year))[2:]

        elif f == 'TIME':
            return \
                str(int(value.hour)).rjust(2, '0') + \
                str(int(value.minute)).rjust(2, '0') + \
                str(int(value.second)).rjust(2, '0')

        elif f == 'LATITUDE':
            frac, whole = modf(value)
            return str(int(whole)).rjust(3, '0') + (f"%.4f" % (frac * 60)).rjust(7, '0')
        elif f == 'N/S':
            return value
        elif f == 'LONGITUDE':
            frac, whole = modf(value)
            return str(int(whole)).rjust(3, '0') + (f"%.4f" % (frac * 60)).rjust(7, '0')
        elif f == 'E/W':
            return value
        elif f == 'SPEED':
            return str(value)
        elif f == 'COURSE':
            return str(value)
        elif f == 'ALTITUDE':
            return str(value)
        elif f == 'ODOMETER':
            return str(value)
        elif f == 'IO_STATUS':
            return str(value)
        elif f == 'EVENT_ID':
            return str(value)
        elif f == 'AIN1':
            return str(value)
        elif f == 'AIN2':
            return str(value)
        elif f == 'FIX_MODE':
            return str(value)
        elif f == ('%s_SAT_NO' % self.name):
            return str(value)
        elif f == 'GPS_SAT_NO':
            return str(value)
        elif f == 'HDOP':
            return str(value)

    def load(self, filename: str = "") -> list:
        """
        :param filename: file which consists rows
        :return: list of dicts
        """

        try:
            c = []
            with open(filename, encoding='utf8') as file:
                for line in file:
                    d = self.convert(line[:-1])
                    c.append(d)
            return c
        except:
            raise ValueError

    def convert(self, s: str = '', sep: str = ',') -> dict:
        """
        convert one line from format
        :param s: line
        :param sep: separator
        :return: dict of values
        """

        s = s[:-1]
        data = s.split(sep)
        output = {}

        for i, f in enumerate(self.keys):
            if data[i + 1] != '':

                try:
                    output[f] = self.format(data[i + 1], f)
                except:
                    raise ValueError

        return output

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
            with open(filename, mode="w") as f:
                for el in info:
                    out = ["&REPORT"]
                    for k in self.keys:
                        if k in el.keys():
                            out.append(self.to_format(el[k], k))
                        else:
                            out.append("")
                    f.write(",".join(out) + ";\n")

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
