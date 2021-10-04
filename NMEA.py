from Format import Format


# TODO Nmea
class Nmea(Format):
    def __init__(self):
        pass

    @staticmethod
    def name():
        return "NMEA"

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

    def upload(self, filename: str = ""):
        return
