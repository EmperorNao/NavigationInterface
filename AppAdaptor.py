from Format import *
from formats.SGK_T import SgkT
from formats.NMEA import Nmea
from formats.Statistic import Statistic


FORMATS = {("%s" % SgkT.name()), ("%s" % Nmea.name()), ("%s" % Statistic.name())}


class ValueBuilder:
    """
    class to plot values without deep information about it
    """
    def __init__(self, f: str = "", cur_x: str = "", cur_y: str = "", info: [dict] = None):
        if f not in FORMATS:
            raise KeyError
        self.f = f
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.info = info
        self.form = Factory.create(self.f)

    def get_measures(self) -> ():
        """

        :return: pair of x and y measure
        """
        try:
            return self.form.measure(self.cur_x), \
                   self.form.measure(self.cur_y)
        except:
            raise KeyError

    def plot(self, plotter):
        """
        method that call form to plot values
        :param plotter: plotter to plot
        :return:
        """
        try:
            self.form.plot(self.cur_x, self.cur_y, self.info, plotter)
        except KeyError as ke:
            raise ke
        except ValueError as ve:
            raise ve


class Factory:
    """
    Class to hide logical creation and decision of formats, all new classes must be define here as creatable
    and also realize interface Format to work correct
    """

    def __init__(self):
        pass

    @staticmethod
    def create(format: str) -> Format:
        """

        :param format: format of data
        :return: create Format from given format
        """
        if format == SgkT.name():
            return SgkT()
        if format == Nmea.name():
            return Nmea()
        if format == Statistic.name():
            return Statistic()
        else:
            raise ValueError


# TODO Transforming
class Transformer:
    """
    Class that combine knowledge about formats to convert one to another using their self methods and some metadata
    """
    pass
