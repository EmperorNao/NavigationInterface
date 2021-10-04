# TODO: do not use bare except
from datetime import date
from datetime import time


SGK_T = "SGK_T"
NMEA = "NMEA"
FORMATS = {("%s" % SGK_T), ("%s" % NMEA)}


class Format:

    def __init__(self):
        pass

    def value(self, s: str = "", f: str = "") -> float:
        """

        :param s: value to convert
        :param f: format of value
        :return: tuple of value and measure
        """
        return None

    def format(self, s: str, f: str = '') -> tuple:
        """

        :param s: value in str
        :param f: format of value
        :return:
        """
        return None

    def convert(self, s: str = '', sep: str = ','):
        return None

    def load(self, filename: str = "") -> [dict]:
        return None

    def plot(self, format_x, format_y) -> tuple:
        return None


class Sgk_t(Format):

    def __init__(self, name: str = ""):
        self.name = name

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
        elif f == ('%s_SAT_NO' % SGK_T):
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
        elif f == ('%s_SAT_NO' % SGK_T):
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
            return int(s[0:2]) + float(s[2:]) / 60
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
        elif f == ('%s_SAT_NO' % SGK_T):
            return int(s)
        elif f == 'GPS_SAT_NO':
            return int(s)
        elif f == 'HDOP':
            return float(s)

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

        form = ['DEVICE_ID', 'DATE', 'TIME', 'LATITUDE', 'N/S', 'LONGITUDE', 'E/W',
                'SPEED', 'COURSE', 'ALTITUDE', 'ODOMETER', 'IO_STATUS', 'EVENT_ID', 'AIN1', 'AIN2',
                'FIX_MODE', ('%s_SAT_NO' % SGK_T), 'GPS_SAT_NO', 'HDOP']

        for i, f in enumerate(form):
            if data[i + 1] != '':

                try:
                    output[f] = self.format(data[i + 1], f)
                except:
                    raise ValueError

        return output

    def plot(self, format_x: str = "", format_y: str = "", info: [dict] = []) -> tuple:
        try:
            x = [self.value(el[format_x], format_x) for el in info]
            y = [self.value(el[format_y], format_y) for el in info]
            return x, y
        except KeyError as ke:
            raise ke


# TODO Nmea
class Nmea(Format):
    pass


# TODO Transforming
class Transformer:
    pass


class Factory:

    def __init__(self):
        pass

    @staticmethod
    def create(format: str) -> Format:
        """

        :param format: format of data
        :return: create Format from given format
        """
        if format == SGK_T:
            return Sgk_t(format)
        if format == NMEA:
            return Nmea(format)
        else:
            raise ValueError
