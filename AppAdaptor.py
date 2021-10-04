from Format import *


class ValueBuilder:
    """
    class to plot values without deep information about it
    """
    def __init__(self, f: str = "", cur_x: str = "", cur_y: str = "", info: [dict] = None):
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

    def get_values(self) -> ():
        """

        :return: pair of list with x and y given values
        """
        return self.form.plot(self.cur_x, self.cur_y, self.info)